# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])


# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'hotpink','size':15}

# plt.title("Sports Watch Data", fontdict = font1)
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)
# plt.plot(x, y)
# plt.show()

# import random
# import matplotlib.pyplot as plt


# days = list(range(1, 11))
# temp = [random.randint(20, 40) for i in days]


# max_temp = max(temp)
# max_day = temp.index(max_temp) + 1


# plt.plot(days, temp, marker='o')


# plt.scatter(max_day, max_temp)

# plt.title("Daily Temperature (10 Days)")
# plt.xlabel("Days")
# plt.ylabel("Temperature")
# plt.text(5, 18, f"Maximum Temperature: {max_temp}°C on Day {max_day}", ha='center')

# plt.show()



import random
import matplotlib.pyplot as plt


days = list(range(1, 31))
temp = [random.randint(20, 40) for i in days]


max_temp = max(temp)
max_day = temp.index(max_temp) + 1


plt.plot(days, temp, marker='o')


plt.scatter(max_day, max_temp, color='red', s=100)

plt.title("Daily Temperature (10 Days)")
plt.xlabel("Days")
plt.ylabel("Temperature")

plt.text(0.5, 0.05, f"Maximum Temperature: {max_temp}°C on Day {max_day}", ha='center')

plt.show()






















# import random
# import matplotlib.pyplot as plt

# days = list(range(1, 11))
# temperature = [random.randint(20, 40) for _ in days]

# plt.plot(days, temperature, marker='*', color='blue', linestyle='-')

# plt.xlabel("Day")
# plt.ylabel("Temperature (°C)")
# plt.title("Random Temperature Data Graph")

# plt.grid(True)
# plt.show()