# 8) Write a program that will calculate the price for a quantity entered from the keyboard, given that the unit price is Rs 5 and there is a discount of 10 percent for quantities over 30 and a 15
# percent discount for quantities over 50.

# Constants
UNIT_PRICE = 5

# Get user input
quantity = int(input("Enter the quantity: "))

# Determine discount
if quantity > 50:
    discount = 0.15  # 15% discount
elif quantity > 30:
    discount = 0.10  # 10% discount
else:
    discount = 0.0   # No discount

# Calculate total price
total_price = quantity * UNIT_PRICE * (1 - discount)

# Display result
print(f"Total price after discount: Rs {total_price:.2f}")
