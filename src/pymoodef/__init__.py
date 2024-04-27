# read version from installed package
from importlib.metadata import version
__version__ = version("pymoodef")

# populate package namespace
from pymoodef.pymoodef import Questions
