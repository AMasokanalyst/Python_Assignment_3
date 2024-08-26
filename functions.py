
# Creating a function called calc_discount
def calc_discount(price, discount_percent):
     # Check if discount percentage is 20% or higher
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price
       

# Prompting the user for input
try:
    price = float(input("Enter the price of the item: "))
    discount_percent = int(input("Enter the discount percentage: "))

    # Calculating the final price
    final_price = calc_discount(price, discount_percent)

    # Printing the final price
    if discount_percent >= 20:
        print(f"The final price after applying a {discount_percent}% discount is: R{final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: R{price:.2f}")

except ValueError:
    print("Invalid input. Please enter numerical values for the price and discount percentage.")
