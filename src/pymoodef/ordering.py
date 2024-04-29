def _generate_ordering(answer, rest, correct_feedback, partially_correct_feedback, incorrect_feedback, orientation):
    if orientation == 'h':
        orientation = 'HORIZONTAL'
    else:
        orientation = 'VERTICAL'
    question = f"""
    <defaultgrade>1</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <layouttype>{orientation}</layouttype>
    <selecttype>ALL</selecttype>
    <selectcount>0</selectcount>
    <gradingtype>ABSOLUTE_POSITION</gradingtype>
    <showgrading>SHOW</showgrading>
    <numberingstyle>none</numberingstyle>
    <correctfeedback format="html">
      <text>{correct_feedback}</text>
    </correctfeedback>
    <partiallycorrectfeedback format="html">
      <text>{partially_correct_feedback}</text>
    </partiallycorrectfeedback>
    <incorrectfeedback format="html">
      <text>{incorrect_feedback}</text>
    </incorrectfeedback>
    <shownumcorrect>1</shownumcorrect>
    <answer fraction="1.0000000" format="moodle_auto_format">
      <text>{answer[0]}</text>
    </answer>
"""
    others = ""
    i = 1
    for r in rest:
        i = i + 1
        fraction = "%d.0000000" % i
        others = others + f"""
    <answer fraction="{fraction}" format="moodle_auto_format">
      <text>{r}</text>
    </answer>
"""
    res = question + others + """
    <hint format="html">
      <text></text>
    </hint>
    <hint format="html">
      <text></text>
    </hint>"""
    return(res)
