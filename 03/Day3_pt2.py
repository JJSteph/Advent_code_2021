# 
# Advent of code 2021
# Day 3 pt 2
# 12/3/2021
#  

with open('./input.txt') as f:
    content = f.readlines()

    # Remove \n in each item
    content = [x.strip() for x in content] 

# Oxygen rating 
# Most common
# Favor 1 in ties

old_list = content.copy()

# Use one bit at a time
for digit in range(len(old_list[0])):

    new_list = []

    # Create counts for 1s and 0s
    count_1 = [x[digit] for x in old_list].count('1')

    count_0 = [x[digit] for x in old_list].count('0')

    # Loop through and keep items based on most common bit
    for number in range(len(old_list)):

        if (count_1 >= count_0) and old_list[number][digit] == '1':

            new_list.append(old_list[number])

        elif (count_1 < count_0) and old_list[number][digit] == '0':
            
            new_list.append(old_list[number])

    # Stop when one number left
    if len(new_list) == 1:
        oxygen = new_list[0]
        break

    old_list = new_list.copy()

# CO2 scrubber rating 
# Least common
# Favor 0 in ties
old_list = content.copy()

# Use one bit at a time
for digit in range(len(old_list[0])):

    new_list = []

    # Create counts for 1s and 0s
    count_1 = [x[digit] for x in old_list].count('1')

    count_0 = [x[digit] for x in old_list].count('0')

    # Loop through and keep items based on most common bit
    for number in range(len(old_list)):

        if (count_1 >= count_0) and old_list[number][digit] == '0':

            new_list.append(old_list[number])

        elif (count_1 < count_0) and old_list[number][digit] == '1':
            
            new_list.append(old_list[number])

    # Stop when one number left
    if len(new_list) == 1:
        CO2 = new_list[0]
        break

    old_list = new_list.copy()


print(f'Oxygen binary: {oxygen}; CO2 binary: {CO2}')

print(f'Oxygen decimal: {int(oxygen, 2)}; CO2 decimal: {int(CO2, 2)}')

print(f'Life support rating: {int(oxygen, 2) * int(CO2, 2)}')