# Import libraries
library(tidyverse)
library(readr)
library(stringr)
# Import cars data
cars <- datasets::mtcars
cars %>% glimpse()

df <- tribble(
  ~name, ~age, ~height,
  "Alice", 14, 1.5,
  "Bob", 13, 1.6,
  "Charlie", 13, 1.7,
  "Dennis", 14, 1.8
)

df %>% glimpse()