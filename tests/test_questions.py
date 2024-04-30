from pymoodef.questions import Questions

class TQuestions(Questions):
    def __init__(self):
        super(Questions, self).__init__()

    def tcategory(self):
        return(self._Questions__category)

    def tlicense(self):
        return(self._Questions__license)

    def tadapt_images(self):
        return(self._Questions__adapt_images)

    def tpath(self):
        return(self._Questions__path)

    def tquestions(self):
        return(self._Questions__questions)

    def tformat_questions(self):
        return(self._Questions__format_questions())
 

def test_questions():
    """Test _questions."""
    q = TQuestions()
    
    q.define_ini('tests/questions.ini')
    v = q.tcategory()
    result = "Initial test"
    assert v == result, "Category it is not correct!"
    v = q.tlicense()
    result = "License Creative Commons Attribution-ShareAlike 4.0"
    assert v == result, "License it is not correct!"
    v = q.tadapt_images()
    result = "true"
    assert v == result, "adapt_images it is not correct!"
    
    q.define_from_csv('tests/questions.csv')
    v = q.tpath()
    result = "tests"
    assert v == result, "path it is not correct!"
    v = q.tquestions()
    assert len(v) == 13, "question rows are is not correct!"
    assert len(v.columns) == 8, "question columns are is not correct!"
    
    q.define_from_csv('tests/questions1.csv', ';')
    v = q.tpath()
    result = "tests"
    assert v == result, "path it is not correct!"
    v = q.tquestions()
    assert len(v) == 13, "question rows are is not correct!"
    assert len(v.columns) == 8, "question columns are is not correct!"
    
    q.define_from_excel('tests/questions.xlsx')
    v = q.tpath()
    result = "tests"
    assert v == result, "path it is not correct!"
    v = q.tquestions()
    assert len(v) == 13, "question rows are is not correct!"
    assert len(v.columns) == 8, "question columns are is not correct!"

    q = Questions()
    q.define_ini('tests/questions.ini')
    v = q.generate_xml()
    questions = ''
    result = f"""<?xml version="1.0" encoding="UTF-8"?>
<quiz>
  <question type="category">
    <category> <text>$course$/top/Initial test</text> </category>
    <info format="html"> <text></text> </info>
    <idnumber></idnumber>
  </question>
  {questions}
</quiz>"""
    assert v == result, "generate_xml it is not correct!"


def test_questions2():
    """Test _questions."""
    q = Questions()
    q.define_ini('tests/questions.ini')
    q.define_from_excel('tests/questions.xlsx')
    r = q.generate_xml()
    v = len(r)
    result = 95293
    assert v == result, "Generated xml it is not correct!"

