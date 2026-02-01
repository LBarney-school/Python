#Initial Bank account class
class BankAccount:
    #Initialize and set starting balance to 0
    def __init__(self):
        self.balance = 0.0

    #Deposit method, prints new balance after adding passed value to balance
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"The amount of: ${deposit_amount:.2f} was deposited.\nThe new balance is: ${self.balance:.2f}")

    #Withdraw method, first checks if argument is greater than balance of account
    #If lesser or equal to balance, subtracts from balance and then prints.
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print(f"The amount of: ${withdraw_amount:.2f} was deposited.\nThe new balance is: ${self.balance:.2f}")
        else:
            print("Insufficient funds.")

'''Create a FeeAccount class that inherits from the BankAccount class. 


The FeeAccount class has an additional method called monthlyFee that subtracts $5 from the balance. 


The withdraw method subtracts the float argument and a $2 fee from the balance and displays the amount withdrawn to the screen. 


Again, the withdraw method cannot allow the balance to drop below zero and should display an message to the screen if such an attempt is made.


Write the code to create a FeeAccount object called my_fee_account: 

    deposit $1000 into the account, 
    withdraw $50, 
    and call the monthlyfee method.'''

#New class Fee account, inherits BankAccount
class FeeAccount(BankAccount):
    #Initialization from bank account and set fee amount.
    def __init__(self):
        super().__init__()
        self.FeeAmount = 5.0
        self.WithFeeAmount = 2.0

    #Monthly fee method, checks for amount enough to cover fee, then subtracts and prints new balance.
    def monthlyFee(self):
        if self.balance >= self.FeeAmount:
            self.balance -= self.FeeAmount
            print(f"Monthly Fee of ${self.FeeAmount:.2f} was deducted.\nThe balance is: ${self.balance:.2f}")
        else:
            print("Insufficient funds.")

    # Withdraw method, first checks if argument is greater than balance of account
    # If lesser or equal to balance, subtracts from balance and then prints.
    def withdraw(self, withdraw_amount):
        if (withdraw_amount + self.WithFeeAmount) <= self.balance:
            self.balance -= withdraw_amount
            self.balance -= self.WithFeeAmount
            print(f"The amount of: ${withdraw_amount:.2f} was withdrawn with a ${self.FeeAmount:.2f} fee.\nThe new balance is: ${self.balance:.2f}")
        else:
            print("Insufficient funds.")

my_fee_account = FeeAccount()
error = 1
while error == 1:
    try:
        my_fee_account.deposit(float(input("Please input deposit amount:")))
        error = 0
    except:
        print("Invalid Input")

error = 1
while error == 1:
    try:
        my_fee_account.withdraw(float(input("Please input withdrawl amount:")))
        error = 0
    except:
        print("Invalid Input for Monthly Fee")

my_fee_account.monthlyFee()