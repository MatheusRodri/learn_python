import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
pop = [2.519, 3.692, 5.263, 7.005, 8.911, 10.03, 11.12]

years = [1800,1850] + years
pop = [1.0, 1.262] + pop

plt.plot(years, pop)

plt.xlabel('Year')
plt.ylabel('Population (in billions)')
plt.title('World Population Over Time')
plt.yticks([0,2,4,6,8,10,12])

plt.show()
