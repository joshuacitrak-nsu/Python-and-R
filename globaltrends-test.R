library(globaltrends)
library(tidyverse)

# help(globaltrends)

# https://cran.r-project.org/web/packages/globaltrends/vignettes/globaltrends.html#changing-locations

getwd()
# initialize_db()

# Start DB ----
start_db()
print(ls())

new_control <- add_control_keyword(
    keyword = c("gmail", "maps", "translate", "wikipedia", "youtube"),
    time = "2010-01-01 2020-12-31"
)

dplyr::filter(keywords_control, keyword == "gmail")


new_control

download_control(control = new_control, locations = countries)

?download_control()

download_control(control = new_control,
                 locations = gt.env$countries)

gt.env$countries

# Close DB ----
disconnect_db()
