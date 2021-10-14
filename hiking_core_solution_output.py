################## WRITE SOLUTION TO CSV ######################################

with open(Path(problem_directory + 'optimized_hiking_trails.csv'), 'w') as f:
    f.write('origin,destination,selected_in_path\n')
    for (i,j) in instance.A:
        f.write('%s,%s,%s\n' % (i,j, instance.route[i,j].value))
