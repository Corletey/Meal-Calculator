# This program calculates the total amount of a meal purchased with a fixed tip.

# Get the charge for the food.
food_charge = float(input("Enter the charge for the food: "))

# Calculate the amount of the tip.
tip = round(food_charge * 0.18, 2)

# Calculate the amount of sales tax.
sales_tax = round(food_charge * 0.07, 2)

# Calculate the Total Sum.
total_sum = food_charge + tip + sales_tax

# Display the tip, sales tax, and total sum.
print("Tip: GH₵", tip)
print("Sales tax: GH₵", sales_tax)
print("Total Sum: GH₵", total_sum)