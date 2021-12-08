# 
# Advent of code 2021
# Day 8 pt 1
# 12/8/2021
#  

with open('./input.txt') as f:
    content = f.readlines()

    # Remove \n in each item
    content = [x.strip() for x in content] 

# Keeping part after | delimiter
content = [x.split('|')[1].strip() for x in content]

# Splitting so each set of number is it's own item
content = [x.split() for x in content]

# Look for values that represent 1, 4, 7, or 8
# 1 has 2 letters, 4 has 4 letters, 7 has 3 letters, and 8 has 7 letters

count = 0

for i in range(len(content)):
    for j in range(len(content[i])):

        if len(content[i][j]) in [2, 3, 4, 7]:
            count += 1

print(f'The digits 1, 4, 7, and 8 appear {count} times')