############################### OBJECTIVE FUNCTION ##############################

def hike_distance_rule(model):
    return sum(model.distance[i,j] * model.route[i,j] for (i,j) in model.A)
model.hike_distance = Objective(rule = hike_distance_rule, sense = minimize)
