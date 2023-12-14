import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from plot import plot_pdf, plot_cdf


x = np.linspace(-10, 10, 1000)
f = stats.norm.pdf(x)
F = stats.norm.cdf(x)

plot_pdf(dis_type="Gaussian", title="PDF", x_axis=x, y_axis=f)
plot_cdf(dis_type="Gaussian", title="CDF", x_axis=x, y_axis=F)
