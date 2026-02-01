'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.'''

file_name = input("Enter file name: ")
f = open(file_name,'r')
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
DSPAM_List = []

for line in f:
    if line.startswith("X-DSPAM-Confidence:"):
        for i in nums:
            if line.find(str(i)) != -1:
                result = line[line.find(str(i)):len(line)-1]
                break
        DSPAM_List.append(float(result))
f.close()

add_list = 0
for i in DSPAM_List:
    add_list += i
average = add_list/len(DSPAM_List)

print(average)
