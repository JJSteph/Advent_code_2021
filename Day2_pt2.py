# 
# Advent of code 2021
# Day 2 pt 2
# 12/2/2021
#  

import re

with open('./input.txt') as f:
    content = f.readlines()

    # Remove \n in each item
    content = [x.strip() for x in content] 

hor_coord = 0
ver_coord = 0
aim = 0

for i in range(len(content)):

    direction = re.search('^\w+(?=\s)', content[i])

    direction = direction.group(0)

    number = re.search('\d+$', content[i])

    number = int(number.group(0))

    if direction == 'forward':
        hor_coord += number
        ver_coord += aim * number

    elif direction == 'up':
        aim -= number

    elif direction == 'down':
        aim += number

print(f'The product of the coordinates is: {hor_coord * ver_coord}')