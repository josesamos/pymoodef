from pymoodef.essay import _generate_essay

def test_generate_essay():
    """Test _generate_essay."""
    v = _generate_essay()
    result = """
    <defaultgrade>1</defaultgrade>
    <penalty>0</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <responseformat>editor</responseformat>
    <responserequired>1</responserequired>
    <responsefieldlines>10</responsefieldlines>
    <minwordlimit></minwordlimit>
    <maxwordlimit></maxwordlimit>
    <attachments>0</attachments>
    <attachmentsrequired>0</attachmentsrequired>
    <maxbytes>0</maxbytes>
    <filetypeslist></filetypeslist>
    <graderinfo format="html">
      <text></text>
    </graderinfo>
    <responsetemplate format="html">
      <text></text>
    </responsetemplate>
"""
    assert v == result, "_generate_essay transformed into wrong string!"
