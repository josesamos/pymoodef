from pymoodef.matching import _generate_matching

def test_generate_matching():
    """Test _generate_matching."""
    v = _generate_matching(["Addition", "+"], ["Subtraction<|>-", "Multiplication<|>*"], "Correct.", "Partially correct.", "Incorrect.")
    result = """
    <defaultgrade>1.0000000</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <shuffleanswers>true</shuffleanswers>
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
    <subquestion format="html">
      <text><![CDATA[<p>Addition<br></p>]]></text>
      <answer>
        <text>+</text>
      </answer>
    </subquestion>

    <subquestion format="html">
      <text><![CDATA[<p>Subtraction<br></p>]]></text>
      <answer>
        <text>-</text>
      </answer>
    </subquestion>

    <subquestion format="html">
      <text><![CDATA[<p>Multiplication<br></p>]]></text>
      <answer>
        <text>*</text>
      </answer>
    </subquestion>
"""
    assert v == result, "_generate_matching transformed into wrong string!"
