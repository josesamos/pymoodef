from pymoodef.pymoodef import moodef
import sys

def main():
    """ Generate an xml file from the questions in csv or excel format. 
    
        We can indicate the name of the output file.
        
        Examples
        --------
        python -m pymoodef tests/questions.xlsx 
        python -m pymoodef tests/questions.xlsx result.xml
    """
    if len(sys.argv) == 2:
        res = moodef(file = sys.argv[1])
    elif len(sys.argv) == 3:
        res = moodef(file = sys.argv[1], xml = sys.argv[2])
    else:
        raise Exception('An input file (csv or xlsx) must be indicated. We can also indicate the output xml file or it will be created in the same folder as the input file.')
    print(f'{res} file generated!')
  
if __name__ == "__main__":
    main()
