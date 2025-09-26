# Instructions
# Print the last item from both the list gdp_cap, and the list life_exp; it is information about Zimbabwe.
# Build a line chart, with gdp_cap on the x-axis, and life_exp on the y-axis. Does it make sense to plot this data on a line plot?
# Don't forget to finish off with a plt.show() command, to actually display the plot.

# Setup
import matplotlib.pyplot as plt
gdp_cap = [974.5803384, 5937.029525, 6223.367465, 4797.231267, 13670.07828, 37062.66272, 44056.92692, 5903.500525, 36126.4927, 64304.7847]
life_exp = [43.828, 76.423, 72.301, 65.554, 80.653, 81.235, 79.829, 64.698, 78.782, 81.687]

# Exercise
# Print the last item from both gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()
