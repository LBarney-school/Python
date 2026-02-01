'''6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.'''

text = "X-DSPAM-Confidence:    0.8475"
nums = [0,1,2,3,4,5,6,7,8,9]
result = ""

for i in nums:
    if text.find(str(i)) != -1:
        result = text[text.find(str(i)):len(text)]
        break
print(float(result))