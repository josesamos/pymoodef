from pymoodef.common import _string_to_vector

def _generate_numerical(answer, rest):
    """Generate the sections of the type of question indicated in the name of the function."""
    answer_1 = answer[0]
    if (len(answer) > 1):
        answer_2 = answer[1]
    else:
        answer_2 = 0
    question = f"""
    <defaultgrade>1</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <answer fraction="100" format="moodle_auto_format">
      <text>{answer_1}</text>
      <feedback format="html">
        <text></text>
      </feedback>
      <tolerance>{answer_2}</tolerance>
    </answer>
"""
    others = ''
    for r in rest:
        rv = _string_to_vector(r)
        answer_1 = rv[0]
        if len(rv) > 1:
            answer_2 = rv[1]
        else:
            answer_2 = 0
        others = others + f"""
    <answer fraction="100" format="moodle_auto_format">
      <text>{answer_1}</text>
      <feedback format="html">
        <text></text>
      </feedback>
      <tolerance>{answer_2}</tolerance>
    </answer>
"""
    res = question + others + """
    <unitgradingtype>0</unitgradingtype>
    <unitpenalty>0.1000000</unitpenalty>
    <showunits>3</showunits>
    <unitsleft>0</unitsleft>"""
    return(res)
