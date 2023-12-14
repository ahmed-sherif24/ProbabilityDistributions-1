import numpy as np
import scipy.stats as stats
from plot import plot_pmf, plot_cdf

p = 0.3
rv = stats.bernoulli(p)
x = np.linspace(0, 1, 2)
f = rv.pmf(x)
F = rv.cdf(x)

mean, var = rv.stats(moments="mv")
print(f"mean: {mean}\nVariance: {var}")

plot_pmf(dis_type="Bernoulli", title='PMF', x_axis=x, y_axis=f)
plot_cdf(dis_type="Bernoulli", title='CDF', x_axis=x, y_axis=F)
