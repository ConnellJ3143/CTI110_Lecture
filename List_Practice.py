# First program using lists

# Get three inputs from user
price1 = float(input("Enter the price of first item: $"))
price2 = float(input("Enter the price of second item: $"))
price3 = float(input("Enter the price of third item: $"))

# Create a list holding the user inputs
items = [price1, price2, price3]

# Print the list
print(items)

# Use sum function to add all values in the list
total_price = sum(items)

# Display total_price
print(f"Total cost for all items is ${total_price:.2f}")

print()

print(f"The lowest value in the list is ${min(items):.2f}")
print()

print(f"The highest value in the list is ${max(items):.2f}")

print()

# Add an item into the pre-existing list
items.append(float(input("Enter cost of new item: $")))

print()
print(items)

# Display item at index 0
print(f"The price of your first item was: ${items[0]}")

# Get the number of items in the list
print(f"Total number if items in the list: {len(items)}")

