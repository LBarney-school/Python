'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.

The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.

The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
loop to find the most prolific committer.'''
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
emails = []

for line in fh:
    line.strip()
    if line.startswith("From:"):
        count = count + 1
        temp = []

        temp = line.split(" ")
        emails.append(temp[1].rstrip())
emails_numbers = dict()
for names in emails:
    if names not in emails_numbers:
        emails_numbers[names] = 1
    else:
        emails_numbers[names] += 1

big_number = 0
big_user = ""
for users in emails_numbers.keys():
    if emails_numbers[users] > big_number:
        big_number = emails_numbers[users]
        big_user = users

print(big_user, big_number)
