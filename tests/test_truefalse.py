from pymoodef.truefalse import _generate_truefalse

def test_generate_truefalse():
    """Test _generate_truefalse."""
    v = _generate_truefalse(["False"])
    result = """
    <defaultgrade>1.0000000</defaultgrade>
    <penalty>1.0000000</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <answer fraction="100" format="moodle_auto_format">
      <text>false</text>
      <feedback format="html">
        <text></text>
      </feedback>
    </answer>
    <answer fraction="0" format="moodle_auto_format">
      <text>true</text>
      <feedback format="html">
        <text></text>
      </feedback>
    </answer>
"""
    assert v == result, "_generate_truefalse transformed into wrong string!"
    v = _generate_truefalse(["True"])
    result = """
    <defaultgrade>1.0000000</defaultgrade>
    <penalty>1.0000000</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <answer fraction="100" format="moodle_auto_format">
      <text>true</text>
      <feedback format="html">
        <text></text>
      </feedback>
    </answer>
    <answer fraction="0" format="moodle_auto_format">
      <text>false</text>
      <feedback format="html">
        <text></text>
      </feedback>
    </answer>
"""
    assert v == result, "_generate_truefalse transformed into wrong string!"
