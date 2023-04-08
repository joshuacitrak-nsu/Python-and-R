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

# Extract parameter samples
alpha_samples = fit['alpha'].flatten()
beta_samples = fit['beta'].flatten()
sigma_samples = fit['sigma'].flatten()

# Create a summary DataFrame using pandas
summary_df = pd.DataFrame({'alpha': alpha_samples, 'beta': beta_samples, 'sigma': sigma_samples})
summary_df = summary_df.describe().transpose().reset_index()
summary_df.columns = ['parameter', 'count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']

print(summary_df)

lower_bound = 0.001
upper_bound = 0.00179

# Check if each beta_sample is within the given range
within_range = (beta_samples >= lower_bound) & (beta_samples <= upper_bound)

# Calculate the mean of the boolean array, which gives the probability
probability = within_range.mean()

print("Probability that beta is within the range:", probability)

import matplotlib.pyplot as plt
import numpy as np

# Prepare data for plotting
num_chains = 4
iterations = 1000
song_age_samples = beta_samples.reshape((num_chains, iterations))

# Create a custom color cycle for the plot
colors = plt.cm.viridis(np.linspace(0, 1, num_chains))

# Create the plot
fig, ax = plt.subplots()
for i, chain in enumerate(song_age_samples):
    ax.plot(np.arange(1, iterations + 1), chain, color=colors[i], label=f"Chain {i + 1}", linewidth=0.6)

ax.set_xlabel("Iteration")
ax.set_ylabel("Song Age")
ax.legend(title="Chain", loc="upper right")

# Set minimal theme
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)

plt.show()
