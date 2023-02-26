# Job: Converting text strings into dates

# The lubridate package has many intuitive functions for parsing dates
library(lubridate)
string_of_text <- c("02-02-22", "02/09/2022", "02.07.2022")
string_of_text
class(string_of_text)

# Specify the desired %d%m%Y format
date_string <- dmy(string_of_text)

year(date_string)
month(date_string)
day(date_string)

date_string
class(date_string)


