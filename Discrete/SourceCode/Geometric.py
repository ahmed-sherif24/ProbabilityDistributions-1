import numpy as np

p = float(input("Enter the probability of success (p): "))

random_variable = np.random.geometric(p)

pmf = (1 - p) ** np.arange(random_variable) * p

mean = np.mean(pmf)

variance = np.var(pmf)

print("Random Variable:", random_variable)
print("PMF:", pmf)
print("Mean:", mean)
print("Variance:", variance)