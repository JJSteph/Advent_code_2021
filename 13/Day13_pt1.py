# 
# Advent of code 2021
# Day 12 pt 1
# 11/20/2022
#  

import re
import copy

with open('./input.txt') as f:
    content = f.readlines()

# Remove \n in each item
content = [x.strip() for x in content] 


def main():

    # Find coordinates in input text

    # Getting match objects
    coords_match = [re.search('\d+,\d+', x) for x in content]

    # Returning the matched text
    coords = []

    # Keeping the coords in new list
    for i in range(len(coords_match)):

        try:
            coords.append(coords_match[i].group())
        except:
            continue

    # Split and conver to int

    coords = [re.split(',', x) for x in coords]

    coords = [[int(y) for y in x] for x in coords]


    # Get max of x and y

    max_x, max_y = 0, 0

    for i in range(len(coords)):

        if coords[i][0] > max_x:
            max_x = coords[i][0]

        if coords[i][1] > max_y:
            max_y = coords[i][1]

    # Creating grid (list of lists)

    grid = [['.' for y in range(max_x + 1)] for x in range(max_y + 1)]


    # Plotting hashes

    for i in range(len(coords)):

        grid[coords[i][1]][coords[i][0]] = '#'


    # Folding instructions

    # Getting match objects
    fold_xy_match = [re.search('(?<=fold along )[x|y](?=\=)', x) for x in content]

    fold_num_match = [re.search('(?<=\=)\d+$', x) for x in content]

    # Returning the matched text

    # Keeping the coords in new list

    fold_instr = []

    for i in range(len(fold_xy_match)):

        try:
            fold_instr.append([fold_xy_match[i].group(), int(fold_num_match[i].group())])
        except:
            continue

    # Looping through folds:

    folds = 1

    for i in range(folds):

        fold_num = fold_instr[i][1]

        if fold_instr[i][0] == 'y':
            
            fold_grid = grid[0:fold_num]

            # Using other hashes

            for j in range(len(grid[fold_num + 1:])):

                for k in range(len(grid[fold_num + j])):

                    if grid[fold_num + 1 + j][k] == '#':
                        fold_grid[len(fold_grid) - 1 - j][k] = '#'
                    else:
                        continue


        elif fold_instr[i][0] == 'x':
            
            fold_grid = [x[0:fold_num] for x in grid]

            # Using other hashes

            for j in range(len(grid)):

                for k in range(len(grid[j][fold_num + 1:])):

                    if grid[j][fold_num + 1 + k] == '#':
                        fold_grid[j][len(fold_grid[j]) - 1 - k] = '#'
                    else:
                        continue

        # folded grid is now just grid
        grid = copy.deepcopy(fold_grid)

    # Count hashes in folded paper:
    hash_count = 0

    for i in range(len(fold_grid)):
        for j in range(len(fold_grid[i])):

            if fold_grid[i][j] == '#':
                hash_count += 1

    print(f'Number of hashes after {folds} folds is {hash_count}')

if __name__ == '__main__':
    main()