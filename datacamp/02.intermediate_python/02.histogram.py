import matplotlib.pyplot as plt

# help(plt.hist)

# Example 1
values = [0,0.6,1.4,1.5,1.6,1.9,2.0,2.2,2.4,2.4,2.4,2.5,2.6,2.7,3.0]
plt.hist(values, bins=3)
plt.show()