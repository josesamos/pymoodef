from pymoodef.ddwtos import _generate_ddwtos

def test_generate_ddwtos():
    """Test _generate_ddwtos."""
    v = _generate_ddwtos(["+"], ["-"], "Correct.", "Partially correct.", "Incorrect.")
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
    <dragbox>
      <text>+</text>
      <group>1</group>
    </dragbox>

    <dragbox>
      <text>-</text>
      <group>1</group>
    </dragbox>
"""
    assert v == result, "_generate_ddwtos transformed into wrong string!"
