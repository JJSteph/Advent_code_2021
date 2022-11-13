# 
# Advent of code 2021
# Day 10 pt 2
# 12/10/2021
#  

with open('./input.txt') as f:
    content = f.readlines()

# Remove \n in each item
content = [x.strip() for x in content] 

symbols_list = ['(', '[', '{', '<']

symbols_end_list = [')', ']', '}', '>']

illegal_char_points = {')': 3, ']': 57, '}': 1197, '>': 25137}

incomplete_char_points = {')': 1, ']': 2, '}': 3, '>': 4}

illegal_char_score = [0 for x in range(len(content))]

current_line_list = [None for x in range(len(content))]

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

    # Saving current line
    current_line_list[i] = current_line

# Remove corrupt lines
# Keeping current line status
incomplete_lines = []

for i in range(len(current_line_list)):
    if illegal_char_score[i] == 0:
        incomplete_lines.append(current_line_list[i])

# Calculating score for characters needed to complete row
# Loop through last char (going backwards)

score_list = [0 for x in range(len(incomplete_lines))]

for i in range(len(incomplete_lines)):

    score = 0

    for j in range(1, len(incomplete_lines[i]) + 1, 1):

        score *= 5

        score += incomplete_char_points[symbols_end_list[symbols_list.index(incomplete_lines[i][-j])]]

    score_list[i] = score

# Sort, and get middle value (should always be odd number of items)

score_list.sort()

print(f'Middle incomplete score: {score_list[(len(score_list) // 2)] }')