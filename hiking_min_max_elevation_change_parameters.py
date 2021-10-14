################################ PARAMETERS ###################################

# Elevation change, in feet, of a trail
model.elevation_change_feet = Param(model.A)

# Elevation change, in feet per mile. This is elevation_change_feet / distance
model.elevation_change_feet_per_mile = Param(model.A)
