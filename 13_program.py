# Q14 (7.5 Marks): Write Matplotlib code to:
# • Generate 300 random x,y points
# • Plot a scatter plot
# • Change marker size & color
# • Add grid, title, and axis labels
import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(300)
y = np.random.rand(300)
plt.scatter(x, y, s=50, c='blue', alpha=0.5, marker='o')
plt.grid(True)
plt.title('Scatter Plot of Random Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()