# 
# Advent of code 2021
# Day 10 pt 1
# 12/10/2021
#  

with open('./input.txt') as f:
    content = f.readlines()

# Remove \n in each item
content = [x.strip() for x in content] 

symbols_list = ['(', '[', '{', '<']

symbols_end_list = [')', ']', '}', '>']

illegal_char_points = {')': 3, ']': 57, '}': 1197, '>': 25137}

illegal_char_score = [0 for x in range(len(content))]

for i in range(len(content)):

    current_line = ''

    symbols_count = [0, 0, 0, 0]

    for j in content[i]:

        if j in symbols_list:
            current_line += j
            symbols_count[symbols_list.index(j)] += 1

        else:

            # If a match
            if symbols_list.index(current_line[-1]) == symbols_end_list.index(j):
                symbols_count[symbols_end_list.index(j)] -= 1
                current_line = current_line[:-1]

            # If not a match
            else:
                illegal_char_score[i] = illegal_char_points[j]
                break

print(f'Sum of error scores {sum(illegal_char_score)}')