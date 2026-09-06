#!/usr/bin/env python3
"""
Plots a histogram of student scores for a project.
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Define bin edges
bins = np.arange(0, 101, 10)

# Plot the histogram with black outlines
plt.hist(student_grades, bins=bins, edgecolor='black')

plt.title("Project A")
plt.xlabel("Grades")
plt.ylabel("Number of Students")


plt.xlim(0, 100)
plt.ylim(0, 30)

plt.xticks(np.arange(0, 101, 10))

plt.show()
