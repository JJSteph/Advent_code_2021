# 
# Advent of code 2021
# Day 9 pt 1
# 12/9/2021
#  

with open('./input.txt') as f:
    content = f.readlines()

    # Remove \n in each item
    content = [x.strip() for x in content] 

# Checks to see if it is the lowest spot
# Returns True or False
def lowest_spot(grid, x, y):

    main_number = int(grid[y][x])

    try:
        if y > 0:
            if main_number >= int(grid[y - 1][x]):
                return False
    except:
        pass

    try:
        if y < len(grid):
            if main_number >= int(grid[y + 1][x]):
                return False
    except:
        pass

    try:
        if x > 0:
            if main_number >= int(grid[y][x - 1]):
                return False
    except:
        pass

    try:
        if x < len(grid[y]):
            if main_number >= int(grid[y][x + 1]):
                return False
    except:
        pass

    return True

# Loop through grid

risk_level = []

for i in range(len(content)):
    for j in range(len(content[i])):

        if lowest_spot(content, j, i) == True:
            risk_level.append(int(content[i][j]) + 1)

print(f'Sum of risk level is {sum(risk_level)}')