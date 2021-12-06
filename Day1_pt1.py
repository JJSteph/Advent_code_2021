# 
# Advent of code 2021
# Day 1 pt 1
# 12/1/2021
#  

with open('./input.txt') as f:
    content = f.readlines()

    # Remove \n in each item
    content = [x.strip() for x in content] 

count_increase = 0

for i in range(len(content)):

    if i == 0:
        continue

    else:
        prev_num = int(content[i - 1])
        current_num = int(content[i])

    if current_num > prev_num:
        count_increase = count_increase + 1

print(f'The number of times increased is {count_increase}')