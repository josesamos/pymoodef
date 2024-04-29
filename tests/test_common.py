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
