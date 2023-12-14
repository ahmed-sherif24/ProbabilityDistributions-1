import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


x = np.linspace(-10, 10, 1000)
f = stats.norm.pdf(x)
F = stats.norm.cdf(x)
plt.plot(x, f)
plt.show()
plt.plot(x, F)
plt.show()
