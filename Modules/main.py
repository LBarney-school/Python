# import utilities module
import utilities

# set initial variables
price = 400.00
tax = 0.06
discount = 0.05
tip = 0.20
total = 0

# validate variables
if utilities.input_validator(price, discount, tax, tip):
    print(f"Initial Price: ${price:.2f}")
    # run through different functions and print values after to check functions work as intended
    tempTax = utilities.add_tax(price, tax)
    print(f"Tax: ${tempTax:.2f}")
    tempDiscount = utilities.apply_discount(price, discount)
    print(f"Discount: ${tempDiscount:.2f}")
    tempTip = utilities.calculate_tip(price, tip)
    print(f"Tip: ${tempTip:.2f}")
    total = price + tempTax - tempDiscount + tempTip
    print(f"Total: ${total:.2f}")
else:
    # catch invalid inputs
    print("Invalid Input")
