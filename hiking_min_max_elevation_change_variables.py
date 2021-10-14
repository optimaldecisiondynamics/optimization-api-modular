########################## DECISION VARIABLES #################################

# Maximum elevation change per mile encountered along our hiking path
# Aka, the maximum value of elevation change per mile of any arc in the path selected
model.max_elevation_change_per_mile = Var(within = NonNegativeReals)
