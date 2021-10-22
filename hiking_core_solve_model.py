######################### SOLVE ############################################

# Detect number of threads for the CBC solver to use
threads = multiprocessing.cpu_count()

solver = SolverFactory('cbc')

# Set solver options, such as the number of threads to use and timeout
solver.options['threads'] = threads

solver.options['seconds'] = 60

# Now solve!
results = solver.solve(instance, tee = True)
