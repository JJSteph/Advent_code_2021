# 
# Advent of code 2021
# Day 6 pt 2
# 12/6/2021
#  

with open('./input.txt') as f:
    content = f.readlines()

    # Remove \n in each item
    content = [x.strip() for x in content] 

content = [x.split(',') for x in content][0]

content = [int(x) for x in content]

days = 256

# Create list of frequencies
freq_list = [0 for x in range(9)]

for i in content:

    freq_list[i] += 1

for _ in range(days):

    new_freq_list = [0 for x in range(9)]

    for j in range(8):

        new_freq_list[j] = freq_list[j + 1]

    if freq_list[0] > 0:
        new_freq_list[8] += freq_list[0]
        new_freq_list[6] += freq_list[0]

    freq_list = new_freq_list.copy()

print(f'Number of fish after {days} days: {sum(freq_list)}')