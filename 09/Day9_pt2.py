# 
# Advent of code 2021
# Day 9 pt 2
# 12/10/2021
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


# Calculate basin size
# Input is lowest spot coord
def basin_size(grid, x, y, count = 1, prev_coord = []):

    current_num = int(grid[y][x])

    prev_coord.append([x, y])

    # Check up    
    try:
        if y > 0:
            if (current_num < int(grid[y - 1][x])) and (int(grid[y - 1][x]) != 9) and ([x, (y - 1)] not in prev_coord):
                count += 1
                count = basin_size(grid, x, (y - 1), count, prev_coord)[0]
                prev_coord.append(basin_size(grid, x, (y - 1), count, prev_coord)[1])
    except:
        pass

    # Check down    
    try:
        if y < len(grid):
            if (current_num < int(grid[y + 1][x])) and (int(grid[y + 1][x]) != 9) and ([x, (y + 1)] not in prev_coord):
                count += 1
                count = basin_size(grid, x, (y + 1), count, prev_coord)[0]
                prev_coord.append(basin_size(grid, x, (y + 1), count, prev_coord)[1])
    except:
        pass

    # Check left 
    try:
        if x > 0:
            if (current_num < int(grid[y][x - 1])) and (int(grid[y][x - 1]) != 9) and ([(x - 1), y] not in prev_coord):
                count += 1
                count = basin_size(grid, (x - 1), y, count, prev_coord)[0]
                prev_coord.append(basin_size(grid, (x - 1), y, count, prev_coord)[1])
    except:
        pass
   
    # Check right    
    try:
        if x < len(grid[y]):
            if (current_num < int(grid[y][x + 1])) and (int(grid[y][x + 1]) != 9) and ([(x + 1), y] not in prev_coord):
                count += 1
                count = basin_size(grid, (x + 1), y, count, prev_coord)[0]
                prev_coord.append(basin_size(grid, (x + 1), y, count, prev_coord)[1])
    except:
        pass

    return [count, prev_coord]


# Loop through grid
# Store coordinates of lowest spots
lowest_points_coords = []

for i in range(len(content)):
    for j in range(len(content[i])):

        if lowest_spot(content, j, i) == True:
            lowest_points_coords.append([j, i])

# Calculate sizes of basins
basin_sizes = [None for x in range(len(lowest_points_coords))]

for i in range(len(lowest_points_coords)):
    basin_sizes[i] = basin_size(content, lowest_points_coords[i][0], lowest_points_coords[i][1])[0]

# Reverse sort to identify top 3
basin_sizes.sort(reverse=True)

print(f'The product of the three largest basins is: {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}')