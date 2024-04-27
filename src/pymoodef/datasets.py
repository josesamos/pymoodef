from importlib import resources

def get_questions_xlsx():
    """Get path to example questions xlsx file.

    Returns
    -------
    pathlib.PosixPath
        Path to file.
    """
    with resources.path("pymoodef.data", "questions.xlsx") as f:
        data_file_path = f
    return data_file_path


def get_questions_csv():
    """Get path to example questions csv file.

    Returns
    -------
    pathlib.PosixPath
        Path to file.
    """
    with resources.path("pymoodef.data", "questions.csv") as f:
        data_file_path = f
    return data_file_path
  

def get_question_ini():
    """Get path to example question ini file.

    Returns
    -------
    pathlib.PosixPath
        Path to file.
    """
    with resources.path("pymoodef.data", "question.ini") as f:
        data_file_path = f
    return data_file_path
