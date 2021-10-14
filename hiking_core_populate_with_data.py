#################### POPULATE WITH DATA AND CREATE MODEL INSTANCE ###################

# Find problem instance data via directory
wd = os.path.abspath('')

problem_directory = wd + '/'

# Read in data to create problem instance
data = DataPortal()

data.load(filename = problem_directory + 'location_info.csv',
select = ('location', 'node_type'), param = model.node_type,
index = model.N)
