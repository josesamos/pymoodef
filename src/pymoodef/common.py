from pandas import isna


def _string_to_vector(str):
    """Transforms string into a vector of strings."""
    if isna(str) or str == "":
        res = []
    else:
        res = str.split("<|>")
    return(res)


def _is_numeric(str):
    """Check if it is numeric."""
    try:
        float(str)
        is_dig = True
    except ValueError:
        is_dig = False
    return(is_dig)


def _is_numeric_answer(answer):
    """Check if answer is numeric."""
    if (len(answer) == 1):
        return(_is_numeric(answer[0]))
    elif (len(answer) == 2):
        return(_is_numeric(answer[0]) and _is_numeric(answer[1]))
    return(False)


def _has_gaps(str):
    """Check if it has gaps."""
    return(str.find('[[1]]') != -1 and str.find('[[2]]') != -1)


  
