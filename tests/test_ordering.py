from pymoodef.ordering import _generate_ordering

def test_generate_ordering():
    """Test _generate_ordering."""
    v = _generate_ordering(["6/2"], ["6-2", "6+2", "6*2"], "Correct.", "Partially correct.", "Incorrect.", "h")
    result = """
    <defaultgrade>1</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <layouttype>HORIZONTAL</layouttype>
    <selecttype>ALL</selecttype>
    <selectcount>0</selectcount>
    <gradingtype>ABSOLUTE_POSITION</gradingtype>
    <showgrading>SHOW</showgrading>
    <numberingstyle>none</numberingstyle>
    <correctfeedback format="html">
      <text>Correct.</text>
    </correctfeedback>
    <partiallycorrectfeedback format="html">
      <text>Partially correct.</text>
    </partiallycorrectfeedback>
    <incorrectfeedback format="html">
      <text>Incorrect.</text>
    </incorrectfeedback>
    <shownumcorrect>1</shownumcorrect>
    <answer fraction="1.0000000" format="moodle_auto_format">
      <text>6/2</text>
    </answer>

    <answer fraction="2.0000000" format="moodle_auto_format">
      <text>6-2</text>
    </answer>

    <answer fraction="3.0000000" format="moodle_auto_format">
      <text>6+2</text>
    </answer>

    <answer fraction="4.0000000" format="moodle_auto_format">
      <text>6*2</text>
    </answer>

    <hint format="html">
      <text></text>
    </hint>
    <hint format="html">
      <text></text>
    </hint>"""
    assert v == result, "_generate_ordering transformed into wrong string!"
