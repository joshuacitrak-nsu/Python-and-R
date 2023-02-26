library(tidyverse)

tweets <- read_csv("./data/tweets.csv")

glimpse(tweets)

tweets %>%
    count(lang)

count_lang <- function(df, column) {
    require(dplyr)
    counts = df %>% count(!! sym(column))
    return(counts)
}

count_lang(df = tweets, column = "lang")

# Which is a redundant function because 
# you can just use the native dplyr and base functions:
count(tweets, lang)
table(tweets["lang"])

# Using base R
col <- tweets["lang"]

counts <- table(col)

counts[names(counts) == "en"]
