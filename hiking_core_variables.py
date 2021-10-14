########################## DECISION VARIABLES #################################

# Binary variables to indicate whether an arc (i,j) is selected in our path or not
model.route = Var(model.A, within = Binary)
