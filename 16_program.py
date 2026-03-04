# Q8 (3 Marks): Write Matplotlib code to plot a line graph for:
# x = [1, 2, 3, 4, 5]
# y = [5, 3, 6, 2, 7]
# Add title and labels.

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 3, 6, 2, 7]
plt.plot(x, y, marker='o')
plt.title('Line Graph of Given Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
