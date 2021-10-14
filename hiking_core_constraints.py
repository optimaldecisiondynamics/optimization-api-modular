########################### CONSTRAINTS ########################################

# Arc selection along the path
def path_constraints_rule(model, i):
    if model.node_type[i] == 'source':
        return sum(model.route[i,j] for j in model.N if (i,j) in model.A) - sum(model.route[j,i] for j in model.N if (j,i) in model.A) == 1
    elif model.node_type[i] == 'sink':
        return sum(model.route[i,j] for j in model.N if (i,j) in model.A) - sum(model.route[j,i] for j in model.N if (j,i) in model.A) == -1
    else:
        return sum(model.route[i,j] for j in model.N if (i,j) in model.A) - sum(model.route[j,i] for j in model.N if (j,i) in model.A) == 0
model.path_constraints = Constraint(model.N, rule = path_constraints_rule)
