# 
# Advent of code 2021
# Day 3 pt 1
# 12/3/2021
#  

with open('./input.txt') as f:
    content = f.readlines()

    # Remove \n in each item
    content = [x.strip() for x in content] 

gamma_binary = ''

epsilon_binary = ''

for digit in range(len(content[0])):

    count_0 = 0
    count_1 = 0

    for number in range(len(content)):

        if content[number][digit] == '0':
            count_0 += 1

        if content[number][digit] == '1':
            count_1 += 1

    if count_0 > count_1:

        gamma_binary = gamma_binary + '0'
        epsilon_binary = epsilon_binary + '1'

    else:

        gamma_binary = gamma_binary + '1'
        epsilon_binary = epsilon_binary + '0'


print(f'Gamma binary: {gamma_binary}; Epsilon binary: {epsilon_binary}')

print(f'Gamma decimal: {int(gamma_binary, 2)}; Epsilon decimal: {int(epsilon_binary, 2)}')

print(f'Power consumption: {int(gamma_binary, 2) * int(epsilon_binary, 2)}')