library(tidyverse)

# read in the pumpkin data
pumpkins <- read_csv("https://raw.githubusercontent.com/microsoft/ML-For-Beginners/main/2-Regression/data/US-pumpkins.csv")

# look at the data
pumpkins %>% glimpse()

names(pumpkins)

library(janitor)

pumpkins  <- pumpkins %>%
  clean_names()

names(pumpkins)

# display 5 random rows
pumpkins %>%
    sample_n(5)

# show the average high price by package and color
pumpkins %>%
    group_by(package, color) %>%
    summarize(avg_high_price = mean(high_price))

# analysis of variance of high price by origin, color
model <- aov(high_price ~ origin + color, data = pumpkins)

# print AOV table
summary(model)

# Tukey's HSD test
TukeyHSD(model)

# plot the data
pumpkins %>%
    ggplot(aes(x = color, y = high_price)) +
    geom_boxplot() +
    theme_minimal()