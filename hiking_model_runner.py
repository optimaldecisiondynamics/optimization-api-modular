############################ PACKAGE SETUP ########################################
from pyomo.environ import *

import os

import pandas as pd

from pathlib import Path

import argparse

import script_executor_function as sef

parser = argparse.ArgumentParser()

parser.add_argument('--model', help = 'The name of the optimization model to run',
choices = ['shortest_path', 'min_max_elevation_change'],
default = 'shortest_path')

args = parser.parse_args()

model_name = args.model
print(model_name)

#################### CREATE DICTIONARY FOR EACH MODEL COMPONENT ######################

# Core model files are part of ALL model formulations
# Additional (specific) model files are run depending on the model in question
# Note: Not every model has every model component. Some models may only use core components

# Read in lookup table of model files
model_file_lookup = pd.read_csv('model_file_lookup.csv', index_col = False)

# Create a dictionary for each model component, which details the file to run for the model name and component
set_files = {}

for row in model_file_lookup.Model.iteritems():

    set_files[row[1]] = model_file_lookup[model_file_lookup['Model'] == row[1]][['Sets']].iloc[0]['Sets']

parameter_files = {}

for row in model_file_lookup.Model.iteritems():

    parameter_files[row[1]] = model_file_lookup[model_file_lookup['Model'] == row[1]][['Parameters']].iloc[0]['Parameters']

###
variable_files = {}

for row in model_file_lookup.Model.iteritems():

    variable_files[row[1]] = model_file_lookup[model_file_lookup['Model'] == row[1]][['Variables']].iloc[0]['Variables']

###
objective_files = {}

for row in model_file_lookup.Model.iteritems():

    objective_files[row[1]] = model_file_lookup[model_file_lookup['Model'] == row[1]][['Objective']].iloc[0]['Objective']

###
constraint_files = {}

for row in model_file_lookup.Model.iteritems():

    constraint_files[row[1]] = model_file_lookup[model_file_lookup['Model'] == row[1]][['Constraints']].iloc[0]['Constraints']

###
data_files = {}

for row in model_file_lookup.Model.iteritems():

    data_files[row[1]] = model_file_lookup[model_file_lookup['Model'] == row[1]][['Data']].iloc[0]['Data']

###
instance_files = {}

for row in model_file_lookup.Model.iteritems():

    instance_files[row[1]] = model_file_lookup[model_file_lookup['Model'] == row[1]][['Instance']].iloc[0]['Instance']

###
solve_files = {}

for row in model_file_lookup.Model.iteritems():

    solve_files[row[1]] = model_file_lookup[model_file_lookup['Model'] == row[1]][['Solve']].iloc[0]['Solve']

###
solution_files = {}

for row in model_file_lookup.Model.iteritems():

    solution_files[row[1]] = model_file_lookup[model_file_lookup['Model'] == row[1]][['Solution']].iloc[0]['Solution']


############################# SETS #########################################

# Core model
sef.script_executor(set_files['core'])

# Specific model
sef.script_executor(set_files[model_name])

################################ PARAMETERS ###################################

# Core model
sef.script_executor(parameter_files['core'])

# Specific model
sef.script_executor(parameter_files[model_name])

########################## DECISION VARIABLES #################################

# Core model
sef.script_executor(variable_files['core'])

# Specific model
sef.script_executor(variable_files[model_name])

############################### OBJECTIVE FUNCTION ##############################

# Core model
sef.script_executor(objective_files['core'])

# Specific model
sef.script_executor(objective_files[model_name])

########################### CONSTRAINTS ########################################

# Core model
sef.script_executor(constraint_files['core'])

# Specific model
sef.script_executor(constraint_files[model_name])

#################### POPULATE WITH DATA ###################

# Note: The use of the route_info.csv file depends on the model we run
# Some parameters exist in one model but not the other

# Core model
sef.script_executor(data_files['core'])

# Specific model
sef.script_executor(data_files[model_name])

#################### CREATE MODEL INSTANCE #########################################

# Core model
sef.script_executor(instance_files['core'])

# Specific model
sef.script_executor(instance_files[model_name])

######################### SOLVE ############################################

# In general, we might solve the model differently depending on which model we run
# But for demonstration, we only have 1 core way (and one set of solver parameters) of solving

# Core model
sef.script_executor(solve_files['core'])

# Specific model
sef.script_executor(solve_files[model_name])

# ################## WRITE SOLUTION TO CSV ######################################

# In general, we might have different outputs (e.g., additional variables) depending on the model we run
# But for this demonstration, we are only interested in whether an arc in the network is selected or not

# Core model
sef.script_executor(solution_files['core'])

# Specific model
sef.script_executor(solution_files[model_name])
