import csv
import numpy as np
import matplotlib.pyplot as plt

# Load data
with open("tips.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  data_numpy = np.array(data_list)

# Get data
size = data_numpy[:,6]
tips = np.array(data_numpy[:,1], dtype=float)
bills = np.array(data_numpy[:,0], dtype=float)
tip_percentages = tips/bills

# Plot data
print(f"The average bill amount is ${round(np.mean(bills), 2)}")
print(f"The median bill amount is ${round(np.median(bills), 2)}")
print(f"The smallest bill is ${round(np.min(bills), 2) }")
print(f"The largest bill is ${round(np.max(bills), 2)}")

#Create scatter plot
plt.scatter(size, tip_percentages, color="#BC8F8F")
plt.xlabel("Dinner Party Size")
plt.ylabel("Tip Percentage")
plt.title("Tips by Party Size and Family Size")
plt.savefig("tips_scatter.png")
plt.show()
