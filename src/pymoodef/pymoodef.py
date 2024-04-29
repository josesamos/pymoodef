from pymoodef.questions import Questions
from pathlib import Path
import os

def moodef(file, ini = '', xml = ''):
    """ Generate an xml file from the questions in csv or excel format. 
    
        We can indicate the name of the ini and output files.

        Parameters
        ----------
        file : str
            Path to csv or excel file.

        ini : str
            Path to ini file (optional).

        xml : str
            Path to output xml file (optional).

        Returns
        -------
        str
            Path to output xml file.
        
        Examples
        --------
        res = moodef(file = 'tests/questions.csv')
        
        res = moodef(file = 'tests/questions.csv', xml = 'result.xml')
        
    """
    q = Questions()
    filename, file_extension = os.path.splitext(file)
    if ini == '':
        path_ini = filename + '.ini'
        if Path(path_ini).is_file():
            q.define_ini(path_ini)
    else:   
        q.define_ini(ini)
    if file_extension.lower() == '.csv':
        q.define_from_csv(file)
    elif file_extension.lower() == '.xlsx':
        q.define_from_excel(file)
    else:
        raise Exception('File type not supported (only csv and xlsx are valid).')
    if xml == '':
        path_xml = filename + '.xml'
        q.generate_xml(path_xml)
        return(path_xml)
    else:   
        q.generate_xml(xml)
        return(xml)
