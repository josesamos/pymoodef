from pymoodef.common import string_to_vector

def generate_matching(answer, rest, correct_feedback, partially_correct_feedback, incorrect_feedback):
    
    question = f"""
    <defaultgrade>1.0000000</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <shuffleanswers>true</shuffleanswers>
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
    <subquestion format="html">
      <text><![CDATA[<p>{answer[0]}<br></p>]]></text>
      <answer>
        <text>{answer[1]}</text>
      </answer>
    </subquestion>
"""
    others = ''
    for r in rest:
        rv = string_to_vector(r)
        others = others + f"""
    <subquestion format="html">
      <text><![CDATA[<p>{rv[0]}<br></p>]]></text>
      <answer>
        <text>{rv[1]}</text>
      </answer>
    </subquestion>
"""
    res = question + others 
    return(res)
