from pymoodef.gapselect import _generate_gapselect

def test_generate_gapselect():
    """Test _generate_gapselect."""
    v = _generate_gapselect(["+"], ["-"], "Correct.", "Partially correct.", "Incorrect.")
    result = """
    <defaultgrade>1</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <shuffleanswers>1</shuffleanswers>
    <correctfeedback format="html">
      <text>Correct.</text>
    </correctfeedback>
    <partiallycorrectfeedback format="html">
      <text>Partially correct.</text>
    </partiallycorrectfeedback>
    <incorrectfeedback format="html">
      <text>Incorrect.</text>
    </incorrectfeedback>
    <shownumcorrect/>
    <selectoption>
      <text>+</text>
      <group>1</group>
    </selectoption>

    <selectoption>
      <text>-</text>
      <group>1</group>
    </selectoption>
"""
    assert v == result, "_generate_gapselect transformed into wrong string!"
