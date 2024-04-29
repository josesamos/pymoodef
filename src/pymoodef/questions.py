from pandas import read_csv, read_excel, isna
from warnings import catch_warnings, simplefilter
from configparser import ConfigParser
from PIL import Image
from base64 import b64encode
from pathlib import Path
import tempfile, os
from string import punctuation
from pymoodef.common import _string_to_vector, _is_numeric_answer, _has_gaps
from pymoodef.numerical import _generate_numerical
from pymoodef.shortanswer import _generate_shortanswer
from pymoodef.multichoice import _generate_multichoice
from pymoodef.ordering import _generate_ordering
from pymoodef.ddwtos import _generate_ddwtos
from pymoodef.gapselect import _generate_gapselect
from pymoodef.matching import _generate_matching
from pymoodef.essay import _generate_essay
from pymoodef.truefalse import _generate_truefalse

class Questions:
    """Defines a set of questions to be included in the Moodle question bank."""

    def __init__(self):
        """Initialize attributes."""
        self.__category = 'Default category'
        self.__first_question_number = '1'
        self.__copyright = ''
        self.__license = ''
        self.__correct_feedback = 'Correct.'
        self.__partially_correct_feedback = 'Partially correct.'
        self.__incorrect_feedback = 'Incorrect.'
        self.__adapt_images = 'FALSE'
        self.__width = '800'
        self.__height = '600'
        self.__questions = None
        self.__path = None

    def define_ini(self, file):
        """Define configuration values.
    
        These values are associated with each defined question.
    
        Parameters
        ----------
        file : str
            Path to ini file.

        Returns
        -------
        None
    
        Examples
        --------
        >>> q = Questions()
        >>> q.define_ini('tests/question.ini')

        """
        config = ConfigParser()
        config.read(file)
        if 'category' in config['DEFAULT']:
            self.__category = config['DEFAULT']['category']
        if 'first_question_number' in config['DEFAULT']:
            self.__first_question_number = config['DEFAULT']['first_question_number']
        if 'copyright' in config['DEFAULT']:
            self.__copyright = config['DEFAULT']['copyright']
        if 'license' in config['DEFAULT']:
            self.__license = config['DEFAULT']['license']
        if 'correct_feedback' in config['DEFAULT']:
            self.__correct_feedback = config['DEFAULT']['correct_feedback']
        if 'partially_correct_feedback' in config['DEFAULT']:
            self.__partially_correct_feedback = config['DEFAULT']['partially_correct_feedback']
        if 'incorrect_feedback' in config['DEFAULT']:
            self.__incorrect_feedback = config['DEFAULT']['incorrect_feedback']
        if 'adapt_images' in config['DEFAULT']:
            self.__adapt_images = config['DEFAULT']['adapt_images']
        if 'width' in config['DEFAULT']:
            self.__width = config['DEFAULT']['width']
        if 'height' in config['DEFAULT']:
            self.__height = config['DEFAULT']['height']
  
    def define_from_csv(self, file, sep = ','):
        """Define questions from a csv file.
    
        Each question is in a row. Each concept in a column.
    
        Parameters
        ----------
        file : str
            Path to csv file.
        sep : str
            Separator character, ',' or ';'.
    
        Returns
        -------
        None
    
        Examples
        --------
        >>> q = Questions()
        >>> q.define_from_csv('tests/questions0.csv')

        """
        self.__path =  "%s" % Path(file).parent
        self.__questions = read_csv(file, sep = sep)
  
    def define_from_excel(self, file, sheet_index = 0):
        """Define questions from an Excel file.
    
        Each question is in a row. Each concept in a column.
    
        Parameters
        ----------
        file : str
            Path to Excel file.
        sheet_index : int
            Number of sheet to process.
    
        Returns
        -------
        None
    
        Examples
        --------
        >>> q = Questions()
        >>> q.define_from_excel('tests/questions.xlsx')

        """
        self.__path = "%s" % Path(file).parent
        with catch_warnings():
            simplefilter("ignore") 
            self.__questions = read_excel(file, sheet_index)

    def generate_xml(self, file):
        """Generate quiz in XML file.
    
        Each question is in a row. Each concept in a column.
    
        Parameters
        ----------
        file : str
            Path to csv file.

        Returns
        -------
        None
    
        Examples
        --------
        >>> q = Questions()
        >>> q.define_from_csv('tests/questions0.csv')
        >>> q.generate_xml('questions.xml')

        """
        questions = self.__format_questions()
        with open(file, "w") as text_file:
            text_file.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<quiz>
  <question type="category">
    <category> <text>$course$/top/{self.__category}</text> </category>
    <info format="html"> <text></text> </info>
    <idnumber></idnumber>
  </question>
  {questions}
</quiz>""")

    def __format_questions(self):
        columns = self.__questions.columns
        columns = columns.difference(['type', 'question', 'image', 'image_alt', 'answer']) 
        res = ''
        for index, row in self.__questions.iterrows():
            res = res + self.__generate_question(row, index, columns)
        return res


    def __get_rest_of_answers(self, row, columns):
        res = []
        for col in columns:
            if not isna(row[col]):
                res.append(row[col])
        return res


    def __generate_question_text(self, row):
        if isna(row['image']):
            img = ''
            fimg = ''
        else:
            file = Path(row['image']).name
            filename, file_extension = os.path.splitext(file)
            image_alt = row['image_alt']
            image = Image.open(self.__path + '/' + row['image'])
            if self.__adapt_images:
                image.thumbnail((int(self.__width), int(self.__height)))
            width, height = image.size
            fd, path = tempfile.mkstemp(suffix=file_extension)
            image.save(path)
            with open(path, "rb") as image_file:
                value = b64encode(image_file.read()).decode('ascii')
            img = f'<p><img src="@@PLUGINFILE@@/{file}" alt="{image_alt}" width="{width}" height="{height}" class="img-fluid atto_image_button_text-bottom"></p>'
            fimg = f'<file name="{file}" path="/" encoding="base64">{value}</file>'
            
        res = f"""
    <questiontext format="html">
      <text><![CDATA[
         <!-- {self.__copyright} -->
         <!-- {self.__license} -->
         <p>{row['question']}</p>{img}]]></text>
         {fimg}
    </questiontext>
    <generalfeedback format="html"> <text></text> </generalfeedback>
"""
        return res

    def __generate_name(self, row, index, type):
        num = int(self.__first_question_number) + index
        question = row['question'][:40]
        for p in punctuation:
            question = question.replace(p, "")
        question = question.replace(" ", "_")
        name = "q%03d_%s_%s" % (num, type, question)
        name = name.lower()
      
        res = f"""
      <name> <text>{name}</text> </name>
"""
        return res
      

    def __generate_question(self, row, index, columns):
        questiontext = self.__generate_question_text(row)
        rest = self.__get_rest_of_answers(row, columns)
        answer = _string_to_vector(row["answer"])
        if _is_numeric_answer(answer):
            type = 'numerical'
            question_type = '<question type="numerical">'
            question_body = _generate_numerical(answer, rest)
        elif len(rest) > 0:
            if len(answer) == 1:
                if not _has_gaps(row["question"]):
                    if isna(row["type"]):
                        type = 'multichoice'
                        question_type = '<question type="multichoice">'
                        question_body = _generate_multichoice(answer, rest, self.__correct_feedback, self.__incorrect_feedback)
                    else:
                        if row["type"].lower() == 'h':
                            orientation = 'h'
                        else:
                            orientation = 'v'
                        type = 'ordering'
                        question_type = '<question type="ordering">'
                        question_body = _generate_ordering(answer, rest, self.__correct_feedback, self.__partially_correct_feedback, self.__incorrect_feedback, orientation)
                else:
                    if isna(row["type"]):
                        type = 'ddwtos'
                        question_type = '<question type="ddwtos">'
                        question_body = _generate_ddwtos(answer, rest, self.__correct_feedback, self.__partially_correct_feedback, self.__incorrect_feedback)
                    else:
                        type = 'gapselect'
                        question_type = '<question type="gapselect">'
                        question_body = _generate_gapselect(answer, rest, self.__correct_feedback, self.__partially_correct_feedback, self.__incorrect_feedback)
            else:
                type = 'matching'
                question_type = '<question type="matching">'
                question_body = _generate_matching(answer, rest, self.__correct_feedback, self.__partially_correct_feedback, self.__incorrect_feedback)
        else:
            if len(answer) == 0:
                type = 'essay'
                question_type = '<question type="essay">'
                question_body = _generate_essay()
            else:
                if answer[0].lower() in ['true', 'false']:
                    type = 'truefalse'
                    question_type = '<question type="truefalse">'
                    question_body = _generate_truefalse(answer)
                else:
                    type = 'shortanswer'
                    question_type = '<question type="shortanswer">'
                    question_body = _generate_shortanswer(answer)

        name = self.__generate_name(row, index, type)
        res = """
""" + question_type + name  + questiontext + question_body + """
</question>"""
        return res


