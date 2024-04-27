from pandas import read_csv, read_excel, isna
from warnings import catch_warnings, simplefilter
from configparser import ConfigParser
from PIL import Image
from base64 import b64encode


class Questions:
    """Defines a set of questions to be included in the Moodle question bank."""

    def __init__(self):
        """Initialize attributes."""
        self.category = 'Default category'
        self.first_question_number = '1'
        self.copyright = ''
        self.license = ''
        self.correct_feedback = 'Correct.'
        self.partially_correct_feedback = 'Partially correct.'
        self.incorrect_feedback = 'Incorrect.'
        self.adapt_images = 'FALSE'
        self.width = '800'
        self.height = '600'
        self.questions = None

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
            self.category = config['DEFAULT']['category']
        if 'first_question_number' in config['DEFAULT']:
            self.first_question_number = config['DEFAULT']['first_question_number']
        if 'copyright' in config['DEFAULT']:
            self.copyright = config['DEFAULT']['copyright']
        if 'license' in config['DEFAULT']:
            self.license = config['DEFAULT']['license']
        if 'correct_feedback' in config['DEFAULT']:
            self.correct_feedback = config['DEFAULT']['correct_feedback']
        if 'partially_correct_feedback' in config['DEFAULT']:
            self.partially_correct_feedback = config['DEFAULT']['partially_correct_feedback']
        if 'incorrect_feedback' in config['DEFAULT']:
            self.incorrect_feedback = config['DEFAULT']['incorrect_feedback']
        if 'adapt_images' in config['DEFAULT']:
            self.adapt_images = config['DEFAULT']['adapt_images']
        if 'width' in config['DEFAULT']:
            self.width = config['DEFAULT']['width']
        if 'height' in config['DEFAULT']:
            self.height = config['DEFAULT']['height']
  
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
        self.questions = read_csv(file, sep = sep)
  
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
            self.questions = read_excel(file, sheet_index)

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
    <category> <text>$course$/top/{self.category}</text> </category>
    <info format="html"> <text></text> </info>
    <idnumber></idnumber>
  </question>
  {questions}
</quiz>""")

    def __format_questions(self):
        res = ''
        for index, row in self.questions.iterrows():
            if isna(row['image']):
                img = ''
                fimg = ''
            else:
                image = Image.open(row['image'])
                if self.adapt_images:
                    image.thumbnail((self.width, self.height))
                width, height = image.size
                img = "row['image']"
                fimg = "row['image_alt']"
            res = res + f"""<questiontext format="html">
      <text><![CDATA[
         <!-- {self.copyright} -->
         <!-- {self.license} -->
         <p>{row['question']}</p>{img}]]></text>
         {fimg}
    </questiontext>
    <generalfeedback format="html"> <text></text> </generalfeedback>"""
        return res
