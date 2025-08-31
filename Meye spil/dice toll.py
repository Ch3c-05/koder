from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np
#
# X = Discrete random variable representing number of successes
# p = Probability of the success
#
X = np.arange(0,21)
p = 0.6
n = 20
#
# Calculate binomial probability distribution
#
binom_pd = binom.pmf(X, n, p)
#
# Plot the probability distribution
#
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(X, binom_pd, 'bo', ms=8, label='geom pmf')
plt.ylabel("Probability", fontsize="18")
plt.xlabel("X - No. of Successes", fontsize="18")
plt.title("Binomial Distribution - No. of Successes Vs Probability", fontsize="18")
ax.vlines(X, 0, binom_pd, colors='b', lw=5, alpha=0.5)
plt.show()