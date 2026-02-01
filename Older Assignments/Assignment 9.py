'''Create a dictionary of a simple restaurant menu (minimum 3 items) where the keys are the menu items and the values
are the prices of those items. Print the list of menu items to the screen and allow the user to select one.
Display the price of the selected item.'''

menu = dict()
menu['pizza'] = '$15.99'
menu['wings'] = '$10.99'
menu['calzone'] = '$12.99'

print("---MENU---")
for item in menu.keys():
    print(item)

print('\n')
selection = input("Which menu item would you like to see the price of? ")

try:
    print(selection + ": " + menu[selection])
except KeyError:
    print("Sorry, the menu item you entered was not found.")