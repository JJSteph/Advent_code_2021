# 
# Advent of code 2021
# Day 4 pt 1
# 12/4/2021
#  

import re

with open('./input.txt') as f:
    content = f.readlines()

    # Remove \n in each item
    content = [x.strip() for x in content] 

# Create grid as nested list

grid = [['.' for x in range(1001)] for x in range(1001)]

for i in content:

    # Parsing coordinates
    first_half = re.search('.*(?=->)', i)
    first_half = first_half.group(0)
    first_half = first_half.strip()

    x1 = re.search('\d+(?=,)', first_half)
    x1 = int(x1.group(0))

    y1 = re.search('(?<=,)\d+', first_half)
    y1 = int(y1.group(0))

    last_half = re.search('(?<=->).*', i)
    last_half = last_half.group(0)
    last_half = last_half.strip()

    x2 = re.search('\d+(?=,)', last_half)
    x2 = int(x2.group(0))

    y2 = re.search('(?<=,)\d+', last_half)
    y2 = int(y2.group(0))


    # Plotting on grid

    if x1 == x2:

        if y2 > y1:

            for i in range(y1,y2 + 1):

                if grid[i][x1] == '.':

                    grid[i][x1] = 1

                else:

                    grid[i][x1] += 1

        else:

            for i in range(y2,y1 + 1):

                if grid[i][x1] == '.':

                    grid[i][x1] = 1

                else:

                    grid[i][x1] += 1



    if y1 == y2:

        if x2 > x1:

            for i in range(x1,x2 + 1):

                if grid[y1][i] == '.':

                    grid[y1][i] = 1

                else:

                    grid[y1][i] += 1

        else:

            for i in range(x2,x1 + 1):

                if grid[y1][i] == '.':

                    grid[y1][i] = 1

                else:

                    grid[y1][i] += 1


# Count coordinates with overlaps (>= 2)

count = 0

for i in range(len(grid)):

    for j in range(len(grid[i])):

        if grid[i][j] != '.':

            if grid[i][j] > 1:

                count += 1


print(f'Number of coordinates with overlap: {count}')