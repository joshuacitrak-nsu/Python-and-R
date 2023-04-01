import stan
import pandas as pd
import nest_asyncio
nest_asyncio.apply()

songs = pd.read_csv('data/radiohead_songs.csv')

songs.head()

# Define the Stan model
stan_code = """
data {
  int<lower=0> N;
  vector[N] song_age;
  vector[N] popularity;
}
parameters {
  real alpha;
  real beta;
  real<lower=0> sigma;
}
model {
  vector[N] mu = alpha + beta * song_age;
  
  // Priors
  alpha ~ normal(0, 100);
  beta ~ normal(0, 100);
  sigma ~ cauchy(0, 5);
  
  // Likelihood
  popularity ~ normal(mu, sigma);
}
"""

# Prepare the data for Stan
data = {
    'N': len(songs),
    'song_age': songs['song_age'].values,
    'popularity': songs['popularity'].values
}

# Compile and run the Stan model
posterior = stan.build(stan_code, data=data, random_seed=1)
fit = posterior.sample(num_chains=4, num_samples=1000)

# Print summary of the Stan model
print(fit)

# Extract parameter samples
alpha_samples = fit['alpha'].flatten()
beta_samples = fit['beta'].flatten()
sigma_samples = fit['sigma'].flatten()

# Create a summary DataFrame using pandas
summary_df = pd.DataFrame({'alpha': alpha_samples, 'beta': beta_samples, 'sigma': sigma_samples})
summary_df = summary_df.describe().transpose().reset_index()
summary_df.columns = ['parameter', 'count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']

print(summary_df)