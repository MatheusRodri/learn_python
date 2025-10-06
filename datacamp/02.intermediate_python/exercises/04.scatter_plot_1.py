# Instructions
# Change the line plot that's coded in the script to a scatter plot.
# A correlation will become clear when you display the GDP per capita on a logarithmic scale. Add the line plt.xscale('log').
# Finish off your script with plt.show() to display the plot.

# Setup
import matplotlib.pyplot as plt
gdp_cap = [974.5803384, 5937.029525, 6223.367465, 4797.231267, 13670.07828, 37062.66272, 44056.92692, 5903.500525, 36126.4927, 64304.7847]
life_exp = [43.828, 76.423, 72.301, 65.554, 80.653, 81.235, 79.829, 64.698, 78.782, 81.687]
# Exercise
# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')


# Show plot
plt.show()
