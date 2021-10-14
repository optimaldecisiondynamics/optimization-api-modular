########################### CONSTRAINTS ########################################

# Maximum elevation change per mile along each arc
def max_elevation_change_per_mile_definition_rule(model, i, j):
    return model.max_elevation_change_per_mile >= model.elevation_change_feet_per_mile[i,j] * model.route[i,j]
model.max_elevation_change_per_mile_definition = Constraint(model.A, rule = max_elevation_change_per_mile_definition_rule)
