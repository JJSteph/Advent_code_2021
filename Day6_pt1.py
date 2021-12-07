# 
# Advent of code 2021
# Day 6 pt 1
# 12/6/2021
#  

with open('./input.txt') as f:
    content = f.readlines()

    # Remove \n in each item
    content = [x.strip() for x in content] 

content = [x.split(',') for x in content][0]

content = [int(x) for x in content]

days = 80

for i in range(days):

    num_new_fish = 0

    # Decrease numbers

    for j in range(len(content)):

        if content[j] > 0:
            content[j] -= 1

        elif content[j] == 0:
            content[j] = 6
            num_new_fish += 1

    # Adding new fish to end of list if needed

    if num_new_fish > 0:
        for _ in range(num_new_fish):

            content.append(8)

# count number of fish in list

print(f'Number of fish after {days} days: {len(content)}')