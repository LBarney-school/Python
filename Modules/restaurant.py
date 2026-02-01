# Imports
import utilities
from Restaurant.Menu import menuLunch, menuDinner
from Restaurant.Tickets import ticketBuild, ticketDrink

# Input for viewing of two different sample tickets to show different functions
exampleType = input(
    "Please enter the type of ticket to see a sample of (1 for Lunch, 2 for Dinner): "
)
if exampleType == "1":
    # Call functions for lunch menu and ticket build
    menuType = menuLunch()
    foodTotal = ticketBuild(menuType, 2, 0, 1)
    drinkTotal = ticketDrink(2, 2, 0)
    mealTotal = foodTotal + drinkTotal
elif exampleType == "2":
    # Call functions for dinner menu and ticket build
    menuType = menuDinner()
    foodTotal = ticketBuild(menuType, 1, 2, 1)
    drinkTotal = ticketDrink(1, 0, 2)
    mealTotal = foodTotal + drinkTotal
else:
    # Catch for invalid selection
    print("Please enter a valid choice.")

# Semi-static variables
tax = 0.06
discount = 0.05
tip = 0.20
total = 0

# Validate variables
if utilities.input_validator(mealTotal, discount, tax, tip):
    print("\n")
    print(f"Subtotal: ${mealTotal:.2f}")
    # run through different functions and print values after to check functions work as intended
    tempTax = utilities.add_tax(mealTotal, tax)
    print(f"Tax: ${tempTax:.2f}")
    tempDiscount = utilities.apply_discount(mealTotal, discount)
    print(f"Discount: ${tempDiscount:.2f}")
    tempTip = utilities.calculate_tip(mealTotal, tip)
    print(f"Tip: ${tempTip:.2f}")
    total = mealTotal + tempTax - tempDiscount + tempTip
    print(f"Total: ${total:.2f}")
else:
    # catch invalid inputs
    print("Invalid Input")
