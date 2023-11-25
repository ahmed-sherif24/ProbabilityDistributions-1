import numpy as np
from scipy.stats import poisson
from Plot import plotting

k = np.arange(0, 16)
print(k)

pmf = poisson.pmf(k, mu=6)
pmf = np.round(pmf, 5)

for val, prob in zip(k, pmf):
    print(f"k-value {val} has probability = {prob}")

plotting(title='Probability Mass Function', x_axis=k, y_axis=pmf)
