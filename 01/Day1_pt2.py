# 
# Advent of code 2021
# Day 1 pt 2
# 12/1/2021
#  

with open('./input.txt') as f:
    content = f.readlines()

    # Remove \n in each item
    content = [x.strip() for x in content] 

count_increase = 0

for i in range(len(content)):

    if i == 0 or i == 1 or (i + 1) >= len(content):
        continue

    else:
        lag_three = int(content[i - 2]) + int(content[i - 1]) + int(content[i])
        lead_three = int(content[i - 1]) + int(content[i]) + int(content[i + 1])

    if lead_three > lag_three:
        count_increase = count_increase + 1

print(f'The number of times increased is {count_increase}')