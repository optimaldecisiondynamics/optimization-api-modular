library(httr)
library(dplyr)

hiking_test <- POST("https://API_URL/mathadelic_woof",
                  body = list(param = upload_file("hiking_inputs.zip")),
                  write_disk("hiking_output.zip", overwrite = TRUE))