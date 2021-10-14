hiking_path_post_processor <- function() {
  ########################################## SETUP #######################################################################
  
  # Read in node set, arc set, and solution
  
  nodes <- read.csv("location_info.csv", header = TRUE, sep = ",", na.strings = "")
  
  arcs <- read.csv("route_info.csv", header = TRUE, sep = ",", na.strings = "")
  
  hiking_solution <- read.csv("optimized_hiking_trails.csv", header = TRUE, sep = ",", na.strings = "")
  
  ################################ PATH PREP ########################################################################
  
  # Derive path by following selected arcs, starting from the source
  solution_selected_arcs <- filter(hiking_solution, selected_in_path == 1)
  
  # We know the path starts from the source, and that any node in the path exists exactly once
  # Find the source node
  node_type_mapper <- select(nodes, location, node_type)
  
  origin_node_types <- merge(solution_selected_arcs, node_type_mapper,
                             by.x = c("origin"),
                             by.y = c("location"))
  
  # first arc starts with the source node
  first_arc_in_path <- filter(origin_node_types,
                              node_type == "source")
  
  other_arcs <- filter(origin_node_types,
                       node_type != "source")
  
  ################################### DERIVE PATH ######################################################################
  
  # Traverse the selected arcs to derive the path, in order
  # Start with the arc containing the source node
  
  # Output a list detailing the path
  # Initialize, then populate
  hiking_path <- c()
  
  # Source node goes first, then the destination node in the first arc
  hiking_path <- c(first_arc_in_path$origin[1], first_arc_in_path$destination[1])
  
  remaining_arcs <- other_arcs
  
  while(nrow(remaining_arcs) != 0) {
    
    # Find the last element in the hiking_path list
    # aka the location we're currently at on our path
    current_node <- tail(hiking_path, n = 1)
    
    # Find an arc that has an origin node == current node
    next_arc <- filter(remaining_arcs, origin == current_node)
    
    # The destination node of next_arc is the next node in our path
    hiking_path <- c(hiking_path, next_arc$destination[1])
    
    # Now that this arc has been added we can remove it from remaining_arcs
    remaining_arcs <- filter(remaining_arcs, origin != current_node)
    
  }
  
  # hiking_path is our optimal path!
  
  ################################## OUTPUT FOR HIKING USER ####################################################
  
  # Output the hiking path to the server's file system
  hiking_path <- data.frame(Hiking_Path = hiking_path)
  
  write.csv(hiking_path, file = "hiking_path_for_the_trail.csv", row.names = FALSE)
  
  # Compute both the distance and maximum elevation change per mile of the path
  # Map the selected arcs back to their parameter values in the arcs dataframe
  arcs_in_hiking_path <- select(solution_selected_arcs, -selected_in_path)
  
  arcs_in_hiking_path <- merge(arcs_in_hiking_path,
                               arcs,
                               by.x = c("origin", "destination"),
                               by.y = c("origin", "destination"))
  
  hiking_path_distance <- sum(arcs_in_hiking_path$distance)
  
  hiking_path_max_elevation_change_feet_per_mile <- max(arcs_in_hiking_path$elevation_change_feet_per_mile)
  
  hiking_path_metrics <- data.frame(Distance = hiking_path_distance,
                                    Max_Elevation_Change_Feet_per_Mile = hiking_path_max_elevation_change_feet_per_mile)
  
  write.csv(hiking_path_metrics, file = "hiking_path_metrics.csv", row.names = FALSE)
  
}