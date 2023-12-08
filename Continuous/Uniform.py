import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform


lower_bound = 0  
upper_bound = 1
rv = uniform(loc=lower_bound, scale=upper_bound - lower_bound)
random_var = rv.rvs(size=1000)
print('Random Variable:', random_var)
x = np.linspace(lower_bound, upper_bound, 100)
pdf = rv.pdf(x)
print('PDF:', pdf)
cdf = rv.cdf(x)
print('CDF:', cdf)
mean = rv.mean()
variance = rv.var()
print('Mean:', mean)
print('Variance:', variance)
plt.plot(x, pdf)
plt.title('Probability Density Function (PDF)')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.show()
plt.plot(x, cdf)
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('x')
plt.ylabel('Cumulative Probability')
plt.show()
