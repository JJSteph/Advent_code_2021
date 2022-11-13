# 
# Advent of code 2021
# Day 11 pt 1
# 12/11/2021
#  

with open('./test.txt') as f:
    content = f.readlines()

# Remove \n in each item
content = [x.strip() for x in content] 



def flash(grid):
    
    








new_grid = [[None for j in range(len(content[i]))] for i in range(len(content))]

for i in range(len(content)):
    for j in range(len(content[i])):

        if content[i][j] == '9':
            new_grid[i][j] = 'X'
            # Flash
            # Then set to 0

        elif content[i][j] == '0':
            new_grid[i][j] = '1'

        else:
            new_grid[i][j] = str(int(content[i][j]) + 1)

