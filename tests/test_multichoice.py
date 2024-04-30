from pymoodef.multichoice import _generate_multichoice

def test_generate_multichoice():
    """Test _generate_multichoice."""
    v = _generate_multichoice(["Addition, subtraction, multiplication and division."], ["Addition and subtraction.", "Addition, subtraction, multiplication, division and square root."], "Correct.", "Incorrect.")
    result = """
    <defaultgrade>1.0000000</defaultgrade>
    <penalty>0.5</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <single>true</single>
    <shuffleanswers>true</shuffleanswers>
    <answernumbering>abc</answernumbering>
    <showstandardinstruction>0</showstandardinstruction>
    <correctfeedback format="moodle_auto_format"> <text>Correct.</text> </correctfeedback>
    <partiallycorrectfeedback format="moodle_auto_format"> <text></text> </partiallycorrectfeedback>
    <incorrectfeedback format="moodle_auto_format"> <text>Incorrect.</text> </incorrectfeedback>
    <answer fraction="100" format="html">
       <text>Addition, subtraction, multiplication and division.</text>
       <feedback format="html"> <text>Correct.</text> </feedback>
    </answer>

    <answer fraction="-50.000000000000000" format="html">
       <text>Addition and subtraction.</text>
       <feedback format="html"> <text>Incorrect.</text> </feedback>
    </answer>

    <answer fraction="-50.000000000000000" format="html">
       <text>Addition, subtraction, multiplication, division and square root.</text>
       <feedback format="html"> <text>Incorrect.</text> </feedback>
    </answer>
"""
    assert v == result, "_generate_multichoice transformed into wrong string!"
