# # import random
# # import matplotlib.pyplot as plt


# # days = list(range(1, 32))
# # income = [random.randint(10000, 50000) for i in days]

# # max_income = max(income)
# # max_day = income.index(max_income) + 1


# # colors = ['blue'] * 31
# # colors[max_day - 1] = 'red'


# # plt.bar(days, income, color=colors)

# # plt.title("Daily Income (31 Days)")
# # plt.xlabel("Days")
# # plt.ylabel("Income")


# # plt.subplots_adjust(bottom=0.2)


# # plt.figtext(0.5, 0.05, f"Maximum Income: ₹{max_income} on Day {max_day}", 
# #             ha='center', fontsize=12, fontweight='bold')

# # plt.show()


# import random
# import matplotlib.pyplot as plt

# days = list(range(1, 32))
# income = [random.randint(10000, 50000) for i in days]

# max_income = max(income)
# max_day = income.index(max_income) + 1

# colors = ['blue'] * 31
# colors[max_day - 1] = 'red'

# plt.figure(figsize=(10,6))


# plt.subplot(2,1,1)
# plt.bar(days, income, color=colors)
# plt.title("Daily Income (Bar Chart)")
# plt.xlabel("Days")
# plt.ylabel("Income")


# plt.subplot(2,1,2)
# plt.plot(days, income, marker='o')
# plt.scatter(max_day, max_income, color='red', s=100)
# plt.title("Daily Income Trend (Line Chart)")
# plt.xlabel("Days")
# plt.ylabel("Income")

# plt.tight_layout()
# plt.show()

import random
import matplotlib.pyplot as plt

days = list(range(1, 32))

salary = [random.randint(20000, 50000) for i in days]
expense = [random.randint(10000, 40000) for i in days]

plt.figure(figsize=(10,6))

plt.plot(days, salary, marker='o', label="Salary Income")
plt.plot(days, expense, marker='o', label="Expense")

plt.title("Salary vs Expense Income (Line Chart)")
plt.xlabel("Days")
plt.ylabel("Amount")
plt.legend()

plt.show()