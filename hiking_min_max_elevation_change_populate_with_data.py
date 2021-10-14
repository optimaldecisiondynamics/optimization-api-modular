#################### POPULATE WITH DATA AND CREATE MODEL INSTANCE ###################

data.load(filename = problem_directory + 'route_info.csv',
select = ('origin', 'destination', 'elevation_change_feet', 'elevation_change_feet_per_mile'),
param = (model.elevation_change_feet, model.elevation_change_feet_per_mile),
index = model.A)
