from numpy.random import normal, seed, uniform
import numpy as np
import matplotlib.pyplot as plt
from functools import partial

plt.rc('figure', dpi=90)
plt.close()

def plot_function(f, title=None, min=-2.1, max=2.1, color='r', ylim=None):
    x = np.linspace(min,max, 100)
    if ylim: plt.ylim(ylim)
    plt.plot(x, f(x), color)
    if title is not None: plt.title(title)
    plt.show()

def quad(a, b, c, x): return a*x**2 + b*x + c

# Define a quadratic function generator
def mk_quad(a, b, c): return partial(quad, a, b, c)

# Specify parameters
f = mk_quad(3, 2, 1)
quad(3,2,1,1.5)
f(1.5)

plot_function(f)

np.random.seed(42)

mu = 0
sigma = 0.1
# draw 1000 samples from the normal distribution 
# s = normal(mu, sigma, 1000)
# s[0:10]
# abs(mu - np.mean(s))
# abs(sigma - np.std(s, ddof=1))
# plt.close()
# count, bins, ignored = plt.hist(s, 30, density = True)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
#          linewidth=2, color='r')
# plt.show()

plt.close()
def noise(x, scale): return normal(scale = scale, size = x.shape)
def add_noise(x, mult, add): return x * (1 + noise(x, mult)) + noise(x, add)

x = np.linspace(-2, 2, 200)
x.shape
y = add_noise(f(x), 0.3, 1.5)
plt.scatter(x, y)

plot_function(f)

plt.show()

normal(scale=0.3, size=x.shape)