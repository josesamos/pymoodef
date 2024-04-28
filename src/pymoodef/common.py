from pandas import isna


def string_to_vector(str):
    """Transforms string into a vector of strings."""
    if isna(str):
        res = []
    else:
        res = str.split("<|>")
    return(res)


def is_numeric(str):
    """Check if it is numeric."""
    try:
        float(str)
        is_dig = True
    except ValueError:
        is_dig = False
    return(is_dig)


def numeric_answer(answer):
    """Check if answer is numeric."""
    return False
