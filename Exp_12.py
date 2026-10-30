import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [15000, 18000, 12000, 20000, 22000, 19000]

plt.bar(months, sales, color='skyblue')
plt.title('Monthly Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales ($)')
plt.show()