# Import libraries
library(dplyr)
library(readr)
library(stringr)
# Import cars data
cars <- read_csv("../python-datacamp/data/cars.csv")

# Base R approach is VERY SIMILAR to PANDAs
cars[["COUNTRY"]] <- toupper(cars[["country"]])

# In dplyr style
cars <- cars %>% mutate(COUNTRY = str_to_upper(country))

# (DON'T DO IT THIS WAY!) We can use apply but too verbose
cars[["COUNTRY"]] <- apply(as.data.frame(cars["country"]),
                           MARGIN = 1, FUN = toupper)

head(cars)

# Alternative base R method
transform(cars, COUNTRY = toupper(cars[["country"]]))

# python-datacamp/