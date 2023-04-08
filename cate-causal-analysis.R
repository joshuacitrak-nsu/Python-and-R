library(tibble)
set.seed(42)

# Number of samples
n <- 1000

# Covariate: age
age <- rnorm(n, mean = 30, sd = 10)

# Treatment variable: job training (random assignment)
treatment <- rbinom(n, size = 1, prob = 0.5)

# True treatment effect (varying with age)
# Here's how the treatment effect varies with age:
# 
# We use the cumulative distribution function of a normal distribution (pnorm) 
# with a mean of 40 and a standard deviation of 10 to create a weight that 
# depends on an individual's age.
# We subtract this weight from 1, so that the treatment effect is larger for 
# younger individuals (with ages less than 40) and smaller for older individuals 
# (with ages greater than 40).
# We multiply this adjusted weight by 500 to scale the treatment effect to a 
# more realistic range.
true_cate <- 500 * (1 - pnorm(age, mean = 40, sd = 10))

# Outcome variable: income
noise <- rnorm(n, mean = 0, sd = 500)
income <- 2000 + 50 * age + treatment * true_cate + noise

# Create the data frame
data <- tibble(age = age, treatment = treatment, income = income)

model <- lm(income ~ treatment * age, data = data)
summary(model)

# The estimated coefficients for treatment, age, and 
# treatment:age represent the treatment effect, the effect of age on income, 
# and the heterogeneous treatment effect (CATE) across different ages, respectively.
