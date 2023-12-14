from scipy.stats import expon
import numpy as np
<<<<<<< HEAD
from plot import plotting
=======
from plot import plot_pdf, plot_cdf
>>>>>>> 290ed34be1f8305beb773596b49cda53556573c3


scale = 2.0
size = 1000
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
<<<<<<< HEAD

x = np.linspace(0, 10, 1000)  # Values of x for plotting
f = expon.pdf(x, scale=scale)  # PDF values
F = expon.cdf(x, scale=scale)  # CDF values

plotting(title="CDF", x_axis=x, y_axis=F)
plotting(title="PDF", x_axis=x, y_axis=f)
=======
x = np.linspace(0, 10, 1000)  # Values of x for plotting
f = expon.pdf(x, scale=scale)  # PDF values
F = expon.cdf(x, scale=scale)  # CDF values

plot_pdf(dis_type="Exponential", title="PDF", x_axis=x, y_axis=f)
plot_cdf(dis_type="Exponential", title="CDF", x_axis=x, y_axis=F)
>>>>>>> 290ed34be1f8305beb773596b49cda53556573c3
