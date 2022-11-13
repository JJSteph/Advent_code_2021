# 
# Advent of code 2021
# Day 7 pt 2
# 12/7/2021
#  

with open('./input.txt') as f:
    content = f.readlines()

    # Remove \n in each item
    content = [x.strip() for x in content] 

content = [x.split(',') for x in content]

content = [int(x) for x in content[0]]

# Try moving all crabs to each possible spot between min and max
# Calculate the difference in abs
# Each difference costs 1 more the longer it gets
# Find the value that results in the smallest sum of differences

unique_spots = [x for x in range(min(content), max(content) + 1)]

# Will store the total fuel needed for each unque spot in this list
fuel_needed = [None for x in range(len(unique_spots))]

for i in range(len(unique_spots)):

    differences = [abs(x - unique_spots[i]) for x in content]

    differences = [(x * (x + 1)) / 2 for x in differences]

    fuel_needed[i] = sum(differences)

print(f'The smallest amount of fuel required is: {int(min(fuel_needed))}')
