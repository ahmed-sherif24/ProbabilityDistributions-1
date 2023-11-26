import numpy as np
import scipy.stats as stats
from Plot import plotting

p = 0.3
rv = stats.bernoulli(p)
x = np.linspace(0, 1, 2)
f = rv.pmf(x)

mean, var = rv.stats(moments="mv")
print(f"mean: {mean}\nVariance: {var}")
plotting(title='Probability Mass Function', x_axis=x, y_axis=f)
