from pathlib import Path
from pymoodef.datasets import get_questions_xlsx, get_questions_csv, get_questions1_csv, get_questions_ini, get_questions1_ini

def test_datasets():
    """Test datasets."""
    
    v = Path(get_questions_xlsx()).name
    result = "questions.xlsx"
    assert v == result, "datasets it is not correct!"
    
    v = Path(get_questions_csv()).name
    result = "questions.csv"
    assert v == result, "datasets it is not correct!"
    
    v = Path(get_questions1_csv()).name
    result = "questions1.csv"
    assert v == result, "datasets it is not correct!"
    
    v = Path(get_questions_ini()).name
    result = "questions.ini"
    assert v == result, "datasets it is not correct!"
    
    v = Path(get_questions1_ini()).name
    result = "questions1.ini"
    assert v == result, "datasets it is not correct!"
    
