from pymoodef.pymoodef import Questions

def test_define_from_csv():
    """Test define questions from a csv file."""
    q0 = Questions()
    q0.define_from_csv('tests/questions0.csv')
    q1 = Questions()
    q1.define_from_csv('tests/questions1.csv', sep = ';')
    assert q0.questions['answer'][0] == q1.questions['answer'][0], "Questions in csv format read incorrectly!"
