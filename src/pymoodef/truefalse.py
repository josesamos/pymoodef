
def generate_truefalse(answer):
    answer_1 = answer[0].lower()
    if answer_1 == 'true':
        answer_2 = 'false'
    else:
        answer_2 = 'true'

    res = f"""
    <defaultgrade>1.0000000</defaultgrade>
    <penalty>1.0000000</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <answer fraction="100" format="moodle_auto_format">
      <text>{answer_1}</text>
      <feedback format="html">
        <text></text>
      </feedback>
    </answer>
    <answer fraction="0" format="moodle_auto_format">
      <text>{answer_2}</text>
      <feedback format="html">
        <text></text>
      </feedback>
    </answer>
"""
    return(res)
