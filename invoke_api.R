library(httr)
library(dplyr)

hiking_test <- POST("http://127.0.0.1:8080/mathematical_hiking",
                  body = list(param = upload_file("hiking_inputs.zip")),
                  write_disk("hiking_output.zip", overwrite = TRUE))