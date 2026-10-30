total_bill = 0.0
while True:
    item_price = input("Enter item price (or type 'done' to finish): ")
    if item_price.lower() == 'done':
        break
    try:
        total_bill += float(item_price)
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"\nYour total bill is: ${total_bill:.2f}")