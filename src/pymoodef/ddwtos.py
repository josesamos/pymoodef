
def generate_ddwtos(answer, rest, correct_feedback, partially_correct_feedback, incorrect_feedback):
    question = f"""
    <defaultgrade>1</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <shuffleanswers>1</shuffleanswers>
    <correctfeedback format="html">
      <text>{correct_feedback}</text>
    </correctfeedback>
    <partiallycorrectfeedback format="html">
      <text>{partially_correct_feedback}</text>
    </partiallycorrectfeedback>
    <incorrectfeedback format="html">
      <text>{incorrect_feedback}</text>
    </incorrectfeedback>
    <shownumcorrect/>
    <dragbox>
      <text>{answer[0]}</text>
      <group>1</group>
    </dragbox>
"""
    others = ""
    for r in rest:
        others = others + f"""
    <dragbox>
      <text>{r}</text>
      <group>1</group>
    </dragbox>
"""
    res = question + others
    return(res)
