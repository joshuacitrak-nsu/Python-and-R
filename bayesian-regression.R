library(tidyverse)
library(rstanarm)
library(tidybayes)
library(broom)
library(broom.mixed)

songs <- read_csv("data/radiohead_songs.csv")
songs %>% glimpse()

stan_model <- stan_glm(popularity ~ song_age, data = songs)

summary(stan_model)

broom.mixed::tidy(stan_model)

posterior_interval(stan_model, prob = 0.77)

# R-squared for Bayesian Model
# Save the variance of residuals

ss_res <- var(residuals(stan_model))

# Save the variance of fitted values
ss_fit <- var(fitted(stan_model))

# Calculate the R-squared
1 - (ss_res / (ss_res + ss_fit))

# Calculate posterior predictive checks

