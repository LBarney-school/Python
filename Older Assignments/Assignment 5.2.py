'''Write a program that invites the user to enter a number between 1 and 10.
Display on the screen a list of multiples of that number which fall between 1 and 100.'''


number = int(input("Please enter a number between 1 and 10:"))
mult = 0
counter = 1
mult_list = []
while True:
    mult = number * counter
    if mult > 100:
        break
    mult_list.append(mult)
    counter += 1

print("The multiples of", number, "are:")
for i in mult_list:
    print(i, end=" ")
