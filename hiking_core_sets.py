############################ SETUP ########################################
from pyomo.environ import *

import os

import pandas as pd

from pathlib import Path

model = AbstractModel()

############################# SETS #########################################

model.N = Set()

model.A = Set(within = model.N * model.N)
