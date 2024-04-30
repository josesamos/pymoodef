from pymoodef.numerical import _generate_numerical

def test_generate_numerical():
    """Test _generate_numerical."""
    v = _generate_numerical(["1.33", "0.03"], [])
    result = """
    <defaultgrade>1</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <answer fraction="100" format="moodle_auto_format">
      <text>1.33</text>
      <feedback format="html">
        <text></text>
      </feedback>
      <tolerance>0.03</tolerance>
    </answer>

    <unitgradingtype>0</unitgradingtype>
    <unitpenalty>0.1000000</unitpenalty>
    <showunits>3</showunits>
    <unitsleft>0</unitsleft>"""
    assert v == result, "_generate_numerical transformed into wrong string!"

    v = _generate_numerical(["2"], ["-2"])
    result = """
    <defaultgrade>1</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <answer fraction="100" format="moodle_auto_format">
      <text>2</text>
      <feedback format="html">
        <text></text>
      </feedback>
      <tolerance>0</tolerance>
    </answer>

    <answer fraction="100" format="moodle_auto_format">
      <text>-2</text>
      <feedback format="html">
        <text></text>
      </feedback>
      <tolerance>0</tolerance>
    </answer>

    <unitgradingtype>0</unitgradingtype>
    <unitpenalty>0.1000000</unitpenalty>
    <showunits>3</showunits>
    <unitsleft>0</unitsleft>"""
    assert v == result, "_generate_numerical transformed into wrong string!"
