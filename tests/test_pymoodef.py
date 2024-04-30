from pymoodef.pymoodef import moodef

def test_pymoodef():
    """Test _questions."""
    
    v = moodef(file='tests/questions.csv')
    result = "tests/questions.xml"
    assert v == result, "moodef it is not correct!"
    
    v = moodef(file='tests/questions1.csv2')
    result = "tests/questions1.xml"
    assert v == result, "moodef it is not correct!"

    v = moodef(file='tests/questions.xlsx')
    result = "tests/questions.xml"
    assert v == result, "moodef it is not correct!"

    
    v = moodef(file='tests/questions.csv', ini='tests/questions1.ini', xml='tests/questions1.xml')
    result = "tests/questions1.xml"
    assert v == result, "moodef it is not correct!"
