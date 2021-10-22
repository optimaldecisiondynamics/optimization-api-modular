######################### SOLVE ############################################

solver = SolverFactory('cbc')

# Set solver options, such as the number of threads to use and timeout
solver.options['threads'] = 2

solver.options['seconds'] = 60

# Now solve!
results = solver.solve(instance, tee = True)
