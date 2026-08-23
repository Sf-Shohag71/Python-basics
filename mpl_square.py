import matplotlib.pyplot as plt

# 1. Prepare data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 2. Create the plot
plt.style.use('seaborn-v0_8')
plt.plot(x, y)
plt.title("My First Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# 3. CRITICAL: Trigger the output window
plt.show()
