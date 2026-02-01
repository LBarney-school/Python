"""The attached file has a list of colors.
Write a program to read from the file and count the number of each color listed.
Print the totals for each color to a new file called colorcount by listing the color and its count on separate lines.
For example:

Red 10
Blue 12
Yellow 3"""

color_file = open("color.txt", "r")
colors = color_file.readlines()
color_list = []
for line in colors:
    color_list.append(line.strip())
color_file.close()

unique_colors = []
for color in color_list:
    if color not in unique_colors:
        unique_colors.append(color)

for color in unique_colors:
    count = 0
    for color_finder in color_list:
        if color == color_finder:
            count += 1
    print(color, count)
