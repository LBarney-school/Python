"""Simulates a bank system that reads user balances and processes withdrawals. It doesn't handle errors or follow code quality standards."""


# Redefinited bank to bank_init to set up initial bank dictionary
def bank_simulation():
    # Initial users setup
    users = {"alice": 1000, "bob": 500, "charlie": 0}
    # Select Withdrawl Target
    withd_target = input("Which account would you like to withdrawl? Input 'N' to skip")
    if withd_target == "N":
        pass
    # Pass if not in Dictionary
    elif withd_target not in users:
        print("Invalid input.")
    # Call Withdrawl if in dictionary
    else:
        temp = withdrawal(withd_target, users[withd_target])
        # Prevention of update when insufficient funds
        try:
            temp = float(temp)
            users[withd_target] = temp
        except:
            print("Unable to Update Withdrawl")
    show_user_summary(users)


# Added new function to allow for withdrawal
def withdrawal(user, balance):
    # Non-numeric input prevention
    try:
        to_withdrawl = float(input(f"Withdraw amount from user {user}: "))
    except:
        print("Invalid input")
    # Greater than balance prevention
    if balance > to_withdrawl:
        return balance - to_withdrawl
    else:
        return print("Insufficient balance")


# Added new function to show user balances
def show_user_summary(users):
    # For each key, print the value
    for key, value in users.items():
        print(f"{key}: ${value:.2f}")


bank_simulation()
