from pymoodef.questions import Questions
from pathlib import Path
import os

def moodef(file, ini = '', xml = ''):
    q = Questions()
    filename, file_extension = os.path.splitext(file)
    path =  ("%s" % Path(file).parent) + '/' + filename
    if ini == '':
        path_ini = path + '.ini'
        if Path(path_ini).is_file():
            q.define_ini(path_ini)
    else:   
        q.define_ini(ini)
    if file_extension.lower() == '.csv':
        q.define_from_csv(file)
    elif file_extension.lower() == '.xlsx':
        q.define_from_xlsx(file)
    else:
        raise Exception('File type not supported (only csv and xlsx are valid).')
    if xml == '':
        path_xml = path + '.xml'
        if Path(path_xml).is_file():
            q.generate_xml(path_xml)
    else:   
        q.generate_xml(xml)

