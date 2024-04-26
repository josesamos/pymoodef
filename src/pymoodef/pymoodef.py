from pandas import read_csv, read_excel
from warnings import catch_warnings, simplefilter
from configparser import ConfigParser


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

    def define_ini(self, file):
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
        self.questions = read_csv(file, sep = sep)
  
    def define_from_excel(self, file, sheet_index = 0):
        with catch_warnings():
            simplefilter("ignore") 
            self.questions = read_excel(file, sheet_index)
