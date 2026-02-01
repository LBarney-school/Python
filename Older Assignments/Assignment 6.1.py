'''Create a function called myemail that takes two arguments: a first name and a last name, and returns a Blue Ridge email address in lower case.

The email is made by taking the first letter of the first name and the first 5 letters of the last name and adding 01 and @my.blueridgectc.edu to the end.

For example, the function call:
    myemail('Amelia','Earhart')
should return
    aearha01@my.blueridgectc.edu'''

def myemail(first_name,last_name):
    domain = 'my.blueridgectc.edu'
    number = '01'
    initial = first_name[0]
    surname = last_name[0:6]
    email = (initial + surname + number + "@" + domain)
    return email.lower()

email = myemail('Amelia','Earhart')
print (email)

