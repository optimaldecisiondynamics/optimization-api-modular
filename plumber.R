library(plumber)
library(purrr)
library(dplyr)
library(zip)

# Source the post processing script as a function
source("./hiking_path_analysis.R")

#* @apiTitle Hiking Path Optimization Problem
#* @apiDescription Use this API to find the best hike for you, depending on your preferences.  Do you prefer to go from origin to destination via the shortest path?  The least steep path?

#* Tell about what the API does
#* @param model_type the type of hiking model to solve (two options: "shortest_path" or "min_max_elevation_change")
#* @serializer contentType list(type="application/octet-stream")
#* @post /mathematical_hiking
function(req, res, model_type = "shortest_path") {
  
  # Upload zip file of data for the optimization model
  multipart <- mime::parse_multipart(req)
  
  fp <- purrr::pluck(multipart, 1, "datapath", 1)
  
  zip::unzip(zipfile = fp, 
             exdir = getwd(), overwrite = TRUE)
  
  # Delete the zip file
  file.remove(fp)
  
  # Run the optimization model!
  system(command = "python3 hiking_model_runner.py",
         wait = TRUE)
  
  # Create folder for solution files
  dir.create("hiking_output")
  
  hiking_path_post_processor()
  
  # copy files to the solution directory
  solution_files <- c("hiking_path_for_the_trail.csv",
                      "hiking_path_metrics.csv")
  file.copy(from = solution_files,
            to = paste0("hiking_output/",
                        solution_files))
  
  # Sending the solution back in a zip file because there are 2 CSVs to send back
  zfile <- tempfile(fileext = ".zip")
  
  zip::zip(zipfile = zfile,
           files = paste0("hiking_output/", solution_files))
  
  readBin(zfile, "raw", n = file.info(zfile)$size)
  
}