from pandas import read_csv, read_excel, isna
from warnings import catch_warnings, simplefilter
from configparser import ConfigParser
from PIL import Image
from base64 import b64encode
from pathlib import Path
import tempfile, os
from string import punctuation
from pymoodef.common import string_to_vector


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
        columns = set(self.__questions.columns)
        columns = columns.difference({'type', 'question', 'image', 'image_alt', 'answer'}) 
        res = ''
        for index, row in self.__questions.iterrows():
            res = res + self.__generate_question(row, index, columns)
        return res
      

    def __generate_question(self, row, index, columns):
        questiontext = self.__generate_question_text(row)
        rest = self.__get_rest_of_answers(row, columns)
        n = len(rest)
        answer = string_to_vector(row["answer"])
        print(answer)
        
        name = self.__generate_name(row, index)
        res = name  + questiontext 
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
            image = Image.open(row['image'])
            if self.__adapt_images:
                image.thumbnail((int(self.__width), int(self.__height)))
            width, height = image.size
            fd, path = tempfile.mkstemp(suffix=file_extension)
            image.save(path)
            value = b64encode(open(path, 'rb').read())
            img = f'<p><img src="@@PLUGINFILE@@/{file}" alt="{image_alt}" width="{width}" height="{height}" class="img-fluid atto_image_button_text-bottom"></p>'
            fimg = f'<file name="{file}" path="/" encoding="base64">{value}</file>'
            
        res = f"""<questiontext format="html">
      <text><![CDATA[
         <!-- {self.__copyright} -->
         <!-- {self.__license} -->
         <p>{row['question']}</p>{img}]]></text>
         {fimg}
    </questiontext>
    <generalfeedback format="html"> <text></text> </generalfeedback>"""
        return res

    def __generate_name(self, row, index):
        num = int(self.__first_question_number) + index
        type = row['type']
        question = row['question'][:40]
        for p in punctuation:
            question = question.replace(p, "")
        question = question.replace(" ", "_")
        if isna(type):
            name = "q%03d_%s" % (num, question)
        else:
            name = "q%03d_%s_%s" % (num, type, question)
        name = name.lower()
      
        res = f'<name> <text>{name}</text> </name>'
        return res


