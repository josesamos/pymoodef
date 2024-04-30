from pymoodef.shortanswer import _generate_shortanswer

def test_generate_shortanswer():
    """Test _generate_shortanswer."""
    v = _generate_shortanswer(["Addition"])
    result = """
    <defaultgrade>1.0000000</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <usecase>0</usecase>
    <answer fraction="100" format="moodle_auto_format">
      <text>Addition</text>
      <feedback format="html">
        <text></text>
      </feedback>
    </answer>
"""
    assert v == result, "_generate_shortanswer transformed into wrong string!"
