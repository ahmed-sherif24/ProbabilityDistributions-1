import numpy as np
from scipy.stats import binom

n = int(input("Enter the number of trials (n): "))
p = float(input("Enter the probability of success (p): "))

random_variable = np.random.binomial(n, p)

pmf = np.random.binomial(n, p, size=n+1) / float(n+1)

mean = np.mean(pmf)

variance = np.var(pmf)

print("Random Variable:", random_variable)
print("PMF:", pmf)
print("Mean:", mean)
print("Variance:", variance)