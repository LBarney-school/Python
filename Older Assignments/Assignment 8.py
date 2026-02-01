'''
Create a list with at least five (5) strings to be used as usernames.

Create a corresponding list of five (5) strings to be used as passwords (one for each username).


Invite the user to enter a username.

If it is in the list, invite them to enter a password.

If the password matches, print a welcome message using their username.

If the user enters a username that is not on the list or enters a password that does not match,
print an appropriate message to inform them.


For example if the usernames were matwood, wshakes, sking, rmunch, jrowlin and passwords were handmaids, hamlet, It,
BeQuiet, Potter then entering sking followed by It would give a welcome message whereas entering sking followed
by Hamlet would not.'''

#variables
usersnames = ['King', 'Anubis', 'Kabhaal', 'Sanket', 'Bastet']
passwords = ['abc123', 'ilikecatsalot', '1giantKreepyD00d', 'WimmyW@mW@m', 'thepasswordonmyluggage']
error_count = 0

#initial input
name = input("Enter your Username: ")
if name in usersnames:
    #grabs 'right' password using index of 'right' name.
    correct_pass = passwords[usersnames.index(name)]
    while error_count < 3:
        pswrd = input("Enter your Password: ")
        if pswrd == correct_pass:
            print(name + ", welcome! Please enjoy your stay.")
            break
        else:
            print("Sorry, your password is incorrect.")
            error_count += 1
else:
    print("Sorry, your username is invalid.")
if error_count >= 3:
    print("Your connection has been locked, please try again later.")

