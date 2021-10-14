#################### POPULATE WITH DATA AND CREATE MODEL INSTANCE ###################

data.load(filename = problem_directory + 'route_info.csv',
select = ('origin', 'destination', 'distance'),
param = (model.distance),
index = model.A)
