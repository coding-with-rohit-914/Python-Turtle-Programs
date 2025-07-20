import matplotlib.pyplot as plt

#data for pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 2, 25, 25]

#data for line graph
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# Creating a pie chart
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)  # 1 row, 2 columns, position 1
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')

# Creating a line graph
plt.subplot(1, 2, 2)  # 1 row, 2 columns, position 2
plt.plot(x, y, marker='o', linestyle='-')
plt.title('Line Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()
