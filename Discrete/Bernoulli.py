import numpy as np
import scipy.stats as stats
from plot import plotting

p = 0.3
rv = stats.bernoulli(p)
x = np.linspace(0, 1, 2)
f = rv.pmf(x)
F = rv.cdf(x)

mean, var = rv.stats(moments="mv")
print(f"mean: {mean}\nVariance: {var}")

plotting(dis_type="Bernoulli", title='PMF', x_axis=x, y_axis=f)
plotting(dis_type="Bernoulli", title='CDF', x_axis=x, y_axis=F)
