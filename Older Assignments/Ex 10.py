'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for
each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting
the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = 0
emails = []

for line in handle:
    line.strip()
    if line.startswith("From "):
        count = count + 1
        temp = []

        temp = line.split(" ")
        emails.append(temp[6].split(":")[0])

emails_count = []
for hours in emails:
    if emails_count.count(hours) < 1:
        emails_count.append(hours)

emails_count.sort()
for hours in emails_count:
    print(hours, emails.count(hours))


