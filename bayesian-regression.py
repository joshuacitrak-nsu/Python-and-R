import stan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
fit = posterior.sample(num_chains=5, num_samples=1000)

callable_methods = [
    method
    for method in dir(fit)
    if (
        callable(getattr(fit, method))
        and not method.startswith('__')
        and not method.startswith('_')
    )
]

print(callable_methods)

fit.to_frame()

# Get posteriors of predicted scores for each observation
y_rep = fit["predicted_popularity"]

# The first 10 rows from each chain (default is 4 chains)
y_rep[:10, :5]

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

# Prepare data for plotting
num_chains = 5
iterations = 1000
song_age_samples = beta_samples.reshape((num_chains, iterations))

# Create a custom color cycle for the plot
colors = plt.cm.viridis(np.linspace(0, 1, num_chains))

# Create the plot of the chain iterations
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

# Compile and run the Stan model
posterior = stan.build(stan_code, data=data, random_seed=1)
fit = posterior.sample(num_chains=5, num_samples=1000)

# Extract parameter samples
alpha_samples = fit['alpha'].flatten()
beta_samples = fit['beta'].flatten()
sigma_samples = fit['sigma'].flatten()

# Define new song ages
new_song_ages = np.array([500, 9000])

# Compute predicted popularity for new song ages using posterior samples ----
predicted_popularity = np.outer(alpha_samples, np.ones_like(new_song_ages)) + \
  np.outer(beta_samples, new_song_ages)

# Predictions for popularity with song age of 500 days
summary_500 = np.percentile(predicted_popularity[:, 0], [2.5, 25, 50, 75, 97.5])

# Predictions for popularity with song age of 9000 days
summary_9000 = np.percentile(predicted_popularity[:, 1], [2.5, 25, 50, 75, 97.5])

print("Mean popularity with song age of 500 days:")
print(round(summary_500[2], 1))

print("Mean popularity with song age of 9000 days:")
print(round(summary_9000[2], 1))

# Create a DataFrame for predicted popularity
predictions_df = pd.DataFrame(predicted_popularity, columns=["500 days", "9000 days"])

# Visualise the distribution using seaborn
predictions_melted = predictions_df.melt(var_name="song_age", value_name="predict")

sns.set_style("whitegrid")
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 8), sharex=True)
fig.subplots_adjust(hspace=0.4)

# Set custom colors
colours = ["#8B008B", "#BDB76B"]

# Add mean labels
mean_9000 = summary_9000[2]
mean_500 = summary_500[2]

# Plot density for 500 days
sns.kdeplot(
    data=predictions_melted[predictions_melted["song_age"] == "500 days"],
    x="predict",
    fill=True,
    common_norm=False,
    alpha=0.8,
    linewidth=0,
    ax=ax1,
    color=colours[0]
    )
ax1.set_title("500 days")
ax1.set_xlabel("")  # remove x-label for the top subplot
ax1.set_ylabel("Density")
ax1.axvline(mean_500, linestyle='--', color='black', label='Mean popularity')
ax1.annotate(f'Mean: {mean_500:.0f}', xy=(mean_500, 0.1), xytext=(mean_500+2.5, 0.25),
             fontsize=12, ha='center', va='center', color='black')

# Plot density for 9000 days
sns.kdeplot(
    data=predictions_melted[predictions_melted["song_age"] == "9000 days"],
    x="predict",
    fill=True,
    common_norm=False,
    alpha=0.8,
    linewidth=0,
    ax=ax2,
    color=colours[1]
)
ax2.set_title("9000 days")
ax2.set_xlabel("Song popularity on Spotify")
ax2.set_ylabel("Density")
ax2.axvline(mean_9000, linestyle='--', color='black', label='Mean popularity')
ax2.annotate(f'Mean: {mean_9000:.0f}', xy=(mean_9000, 0.1), xytext=(mean_9000+2.5, 0.25),
             fontsize=12, ha='center', va='center', color='black')

fig.suptitle("Predicted Radiohead song popularity distributions as a function of song age")
sns.despine()
plt.tight_layout()
plt.show()
