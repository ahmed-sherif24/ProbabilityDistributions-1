import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from numpy import random
from plot import plot_pmf, plot_cdf


# Generate a random 1x10 distribution for occurrence 2:
x = random.poisson(lam=2, size=10)
print(x)

# We will need an array of the k values for which we will compute the Poisson PMF
k = np.arange(0, 16)
print(k)

# Calculate the Poisson PMF
pmf = poisson.pmf(k, mu=6)
pmf = np.round(pmf, 5)
for val, prob in zip(k, pmf):
    print(f"k-value {val} has probability = {prob}")

# Plot Poisson PMF using bar plot
plot_pmf(dis_type="Poisson", title="PMF", x_axis=k, y_axis=pmf)

# Calculate the Poisson CDF
cdf = poisson.cdf(k, mu=7)
cdf = np.round(cdf, 3)
for val, prob in zip(k, cdf):
    print(f"k-value {val} has probability = {prob}")

# Plot Poisson CDF using step plot
plot_cdf(dis_type="Poisson", title="CDF", x_axis=k, y_axis=cdf)

# Calculate the first four moments: expectation, variance
mu = 7
mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
print("Expectation is : \n", mean)
print("Variance is : \n", var)
print("3rd Moment is : \n", skew)
print("4th Moment is : \n", kurt)
