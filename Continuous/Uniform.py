import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
from plot import plotting


lower_bound = 0
upper_bound = 1
rv = uniform(loc=lower_bound, scale=upper_bound - lower_bound)
random_var = rv.rvs(size=1000)
print('Random Variable:', random_var)
x = np.linspace(lower_bound, upper_bound, 100)
f = rv.pdf(x)
print('PDF:', f)
F = rv.cdf(x)
print('CDF:', F)
mean = rv.mean()
variance = rv.var()
print('Mean:', mean)
print('Variance:', variance)


plotting(dis_type="Uniform", title="PDF", x_axis=x, y_axis=f)
plotting(dis_type="Uniform", title="CDF", x_axis=x, y_axis=F)
