# Q12 (4 Marks): Write Matplotlib code to create three vertical subplots, each showing a bar chart with different random data.
import matplotlib.pyplot as plt
import numpy as np
# Generate random data for three bar charts
data1 = np.random.randint(1, 10, size=5)
data2 = np.random.randint(1, 10, size=5)
data3 = np.random.randint(1, 10, size=5)
labels = ['A', 'B', 'C', 'D', 'E']
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 12))
ax1.bar(labels, data1, color='b')
ax1.set_title('Bar Chart 1')
ax2.bar(labels, data2, color='g')
ax2.set_title('Bar Chart 2')
ax3.bar(labels, data3, color='r')
ax3.set_title('Bar Chart 3')    
plt.tight_layout()
plt.show()
    