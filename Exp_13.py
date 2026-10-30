import matplotlib.pyplot as plt

categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transport']
expenses = [1200, 400, 200, 150, 100]

plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Monthly Expense Distribution')
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()