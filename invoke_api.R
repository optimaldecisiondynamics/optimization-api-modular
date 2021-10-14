library(httr)
library(dplyr)

hiking_test <- POST("https://API_URL/mathematical_hiking",
                  body = list(param = upload_file("hiking_inputs.zip")),
                  write_disk("hiking_output.zip", overwrite = TRUE))