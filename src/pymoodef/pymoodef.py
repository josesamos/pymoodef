from pymoodef.questions import Questions

def moodef(file, ini = '', xml = ''):
    q = Questions()
    q.define_ini('tests/question.ini')
    q.define_from_csv('tests/questions0.csv')
    q.generate_xml('questions.xml')
