from pyomo.environ import *

import os

import pandas as pd

from pathlib import Path

def script_executor(file_name):
    """ Input a file name, and execute that file. Do nothing if the file name is NULL. """
    if pd.isnull(file_name) == False:
        return exec(open(file_name).read(), globals())
    else:
        pass
