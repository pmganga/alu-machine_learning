#!/usr/bin/env python3
"""
Plots a stacked bar graph representing fruit ownership.
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

people = ['Farrah', 'Fred', 'Felicia']
bar_width = 0.5

apples = fruit[0]
bananas = fruit[1]
oranges = fruit[2]
peaches = fruit[3]

# Plot each layer
plt.bar(people, apples, width=bar_width, color='red', label='apples')
plt.bar(people, bananas, width=bar_width, bottom=apples,
        color='yellow', label='bananas')
plt.bar(people, oranges, width=bar_width, bottom=apples + bananas,
        color='#ff8000', label='oranges')
plt.bar(people, peaches, width=bar_width,
        bottom=apples + bananas + oranges,
        color='#ffe5b4', label='peaches')

# Set the limits
plt.ylabel("Quantity of Fruit")
plt.title("Number of Fruit per Person")
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))

# Display the legend
plt.legend()

plt.show()