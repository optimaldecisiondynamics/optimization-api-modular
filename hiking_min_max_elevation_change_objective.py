############################### OBJECTIVE FUNCTION ##############################

def hiking_elevation_change_per_mile_rule(model):
    return model.max_elevation_change_per_mile
model.hiking_elevation_change_per_mile = Objective(rule = hiking_elevation_change_per_mile_rule, sense = minimize)
