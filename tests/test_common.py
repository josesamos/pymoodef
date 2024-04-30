import pytest
from pymoodef.common import _string_to_vector, _is_numeric, _is_numeric_answer, _has_gaps

@pytest.mark.parametrize(
    "str, result",
    [
        ("Addition<|>+", ["Addition", "+"]),
        ("Addition", ["Addition"]),
        ("", []),
        (None, [])  
    ]
)
def test_string_to_vector(str, result):
    """Test _string_to_vector."""
    v = _string_to_vector(str)
    assert v == result, "String transformed into wrong vector!"


@pytest.mark.parametrize(
    "str, result",
    [
        ("-34", True),
        ("-34.56", True),
        ("34.56", True),
        ("34", True),
        ("", False),
        ("a23", False),
        ("23a", False),
        ("23.34.56", False)  
    ]
)
def test_is_numeric(str, result):
    """Test _is_numeric."""
    v = _is_numeric(str)
    assert v == result, "Number not correctly detected!"


@pytest.mark.parametrize(
    "str, result",
    [
        (["-34"], True),
        (["-34.56", "2"], True),
        (["34.56", "0.54"], True),
        (["34.56", "0.54", "0.54"], False),
        ([""], False),
        (["a23"], False),
        (["a23", "2"], False)
    ]
)
def test_is_numeric_answer(str, result):
    """Test _is_numeric_answer."""
    v = _is_numeric_answer(str)
    assert v == result, "Numeric answer not correctly detected!"


@pytest.mark.parametrize(
    "str, result",
    [
        ("The [[1]], is [[2]].", True),
        ("The [[2]], is [[1]].", True),
        ("The [[1]], is [[2]], is [[3]].", True),
        ("The [[1]].", False),
        ("", False),
        (None, False)
    ]
)
def test_has_gaps(str, result):
    """Test _has_gaps."""
    v = _has_gaps(str)
    assert v == result, "Gaps not correctly detected!"
