#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt

y = np.arange(0, 11) ** 3

# y as a red line
plt.plot(y, 'r-')

# x axis range from 0 to 10
plt.xlim(0, 10)

plt.show()
