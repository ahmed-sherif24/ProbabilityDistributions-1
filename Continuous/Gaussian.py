import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from plot import plotting


x = np.linspace(-10, 10, 1000)
f = stats.norm.pdf(x)
F = stats.norm.cdf(x)

plotting(dis_type="Gaussian", title="PDF",x_axis=x, y_axis=f)
plotting(dis_type="Gaussian", title="CDF",x_axis=x, y_axis=F)
