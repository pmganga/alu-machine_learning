#!/usr/bin/env python3
"""
Plots a line graph showing the exponential decay of C-14.
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28650)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# Plot as a line graph
plt.plot(x, y)

plt.title("Exponential Decay of C-14")
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")

# x-axis limit
plt.xlim(0, 28650)

# Set y-axis to a log scale
plt.yscale('log')

plt.show()
