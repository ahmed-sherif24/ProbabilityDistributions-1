import numpy as np
import matplotlib.pyplot as plt

n = 6
p = 0.6
r_values = np.arange(n + 1)

dist = np.random.binomial(n, p)

print("r\tp(r)")
for r, prob in zip(r_values, dist):
    print(f"{r}\t{prob}")

mean = n * p
variance = n * p * (1 - p)

print(f"mean = {mean}")
print(f"variance = {variance}")

plt.bar(r_values, dist)
plt.show()
