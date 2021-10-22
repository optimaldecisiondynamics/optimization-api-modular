library(httr)
library(dplyr)

# When running locally
# The port (8080 in this case) must be part of the url
hiking_test <- POST("http://127.0.0.1:8080/mathematical_hiking",
                  body = list(param = upload_file("hiking_inputs.zip")),
                  write_disk("hiking_output.zip", overwrite = TRUE))

# When running on cloud run the port should NOT be included in the url
# E.g., https://your_api_url/mathematical_hiking

# 2 API requests, one for each model type
hiking_test <- POST("https://your_api_url/mathematical_hiking/mathematical_hiking",
                    body = list(param = upload_file("hiking_inputs.zip")),
                    query = list(model_type = "min_max_elevation_change"),
                    write_disk("hiking_output.zip", overwrite = TRUE))

hiking_test2 <- POST("https://your_api_url/mathematical_hiking/mathematical_hiking",
                    body = list(param = upload_file("hiking_inputs.zip")),
                    query = list(model_type = "shortest_path"),
                    write_disk("hiking_output.zip", overwrite = TRUE))