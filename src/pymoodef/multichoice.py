def _generate_multichoice(answer, rest, correct_feedback, incorrect_feedback):
    question = f"""
    <defaultgrade>1.0000000</defaultgrade>
    <penalty>0.5</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <single>true</single>
    <shuffleanswers>true</shuffleanswers>
    <answernumbering>abc</answernumbering>
    <showstandardinstruction>0</showstandardinstruction>
    <correctfeedback format="moodle_auto_format"> <text>{correct_feedback}</text> </correctfeedback>
    <partiallycorrectfeedback format="moodle_auto_format"> <text></text> </partiallycorrectfeedback>
    <incorrectfeedback format="moodle_auto_format"> <text>{incorrect_feedback}</text> </incorrectfeedback>
    <answer fraction="100" format="html">
       <text>{answer[0]}</text>
       <feedback format="html"> <text>{correct_feedback}</text> </feedback>
    </answer>
"""
    value = "-%2.15f" % (100 / len(rest))
    others = ''
    for r in rest:
        others = others + f"""
    <answer fraction="{value}" format="html">
       <text>{r}</text>
       <feedback format="html"> <text>{incorrect_feedback}</text> </feedback>
    </answer>
"""
    res = question + others
    return(res)
