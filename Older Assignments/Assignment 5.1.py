'''Write a program to allow the user to enter five numbers, one at a time.
After each entry, tell the user whether the number is odd or even.
At the end of all the entries, display the sum total of all the entered numbers on the screen.'''

total = 0
for i in range(5):
    try:
        number = int(input('Enter a number: '))
        if number % 2 == 0:
            print(number, "is an even number.")
        else:
            print(number, "is an odd number.")
        total += number
    except ValueError:
        print('Please enter a number.')
        continue

print("The total of all entered numbers is:", total)
