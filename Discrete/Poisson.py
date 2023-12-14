import numpy as np
from scipy.stats import poisson
from plot import plotting

k = np.arange(0, 16)
print(k)

pmf = poisson.pmf(k, mu=6)
pmf = np.round(pmf, 5)

for val, prob in zip(k, pmf):
    print(f"k-value {val} has probability = {prob}")


plotting(dis_type="Poisson", title='PDF', x_axis=x, y_axis=f)
plotting(dis_type="Poisson", title='CDF', x_axis=x, y_axis=F)
