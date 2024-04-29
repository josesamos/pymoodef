def _generate_shortanswer(answer):
    """Generate the sections of the type of question indicated in the name of the function."""
    res = f"""
    <defaultgrade>1.0000000</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <usecase>0</usecase>
    <answer fraction="100" format="moodle_auto_format">
      <text>{answer[0]}</text>
      <feedback format="html">
        <text></text>
      </feedback>
    </answer>
"""
    return(res)
