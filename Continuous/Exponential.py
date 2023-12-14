from scipy.stats import expon
import numpy as np
from plot import plot_pdf, plot_cdf

# Generate random numbers from exponential distribution
scale = 2.0  # The scale parameter (mean = 1 / scale)
size = 1000  # Number of random numbers to generate
random_numbers = expon.rvs(scale=scale, size=size)

# Calculate statistics
mean = expon.mean(scale=scale)
variance = expon.var(scale=scale)
standard_deviation = expon.std(scale=scale)
median = expon.median(scale=scale)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)
print("Median:", median)

# Calculate CDF at a given value
x = 3.0
cdf = expon.cdf(x, scale=scale)
print("CDF at", x, ":", cdf)

# Calculate quantile at a given probability
p = 0.75
quantile = expon.ppf(p, scale=scale)
print("Quantile at", p, ":", quantile)

# Plot the PDF and CDF
x = np.linspace(0, 10, 1000)  # Values of x for plotting
f = expon.pdf(x, scale=scale)  # PDF values
F = expon.cdf(x, scale=scale)  # CDF values

plot_pdf(dis_type="Exponential", title="PDF", x_axis=x, y_axis=f)
plot_cdf(dis_type="Exponential", title="CDF", x_axis=x, y_axis=F)
