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
    """Get path to example questions csv file with "," as separator.

    Returns
    -------
    pathlib.PosixPath
        Path to file.
    """
    with resources.path("pymoodef.data", "questions.csv") as f:
        data_file_path = f
    return data_file_path


def get_questions1_csv():
    """Get path to example questions csv file with ";" as separator.

    Returns
    -------
    pathlib.PosixPath
        Path to file.
    """
    with resources.path("pymoodef.data", "questions1.csv") as f:
        data_file_path = f
    return data_file_path
  

def get_questions_ini():
    """Get path to example questions ini file.

    Returns
    -------
    pathlib.PosixPath
        Path to file.
    """
    with resources.path("pymoodef.data", "questions.ini") as f:
        data_file_path = f
    return data_file_path
  

def get_questions1_ini():
    """Get path to example questions1 ini file.

    Returns
    -------
    pathlib.PosixPath
        Path to file.
    """
    with resources.path("pymoodef.data", "questions1.ini") as f:
        data_file_path = f
    return data_file_path
