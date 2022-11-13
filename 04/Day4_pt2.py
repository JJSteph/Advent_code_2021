# 
# Advent of code 2021
# Day 4 pt 2
# 12/4/2021
#  

# Functions to check for a winner

# Check for an horizontal win
def win_hor(list, width):

    count = 0

    for i in range(len(list)):

        if (i) % width == 0:
            count = 0

        if list[i] == 'X':
            count += 1

        if count == width:
            return True

    return False

# Check for a vertical win
def win_ver(list, width):

    for i in range(width):
        count = 0
        for j in range(i, len(list), width):

            if list[j] == 'X':
                count += 1
            
            # This will only work if width == height (Square boards)
            if count == width:
                return True

    return False


with open('./input.txt') as f:
    content = f.readlines()

    # Remove \n in each item
    content = [x.strip() for x in content] 

# Copy directions into it's own list
directions = content[0].split(',')

# Remove directions from input
content.pop(0)

# Remove first blank
content.pop(0)

## Creating list of boards

boards = []

to_add = ''

for i in range(len(content)):

    if content[i] == '':
        boards.append(to_add)
        to_add = ''

    elif i == len(content) - 1:
        to_add = to_add.strip() + ' ' + content[i].strip()
        boards.append(to_add)

    else:
        to_add = to_add.strip() + ' ' + content[i].strip()

# Splitting each board so each number is an item
boards = [x.split(' ') for x in boards]

# Removing any blank items in board
boards = [[x for x in inner if x != ''] for inner in boards]



winning_board = None

winning_number = None

prev_winning_boards = []

# Place Xs where each item is called
for number in directions:

    for outer in range(len(boards)):

        for inner in range(len(boards[outer])):

            if boards[outer][inner] == number:

                boards[outer][inner] = 'X'

    # Checking for winner

    for i in range(len(boards)):

        if (win_hor(boards[i], 5) or win_ver(boards[i], 5)) and (i not in prev_winning_boards):
            winning_board = i
            winning_number = number
            winning_board_state = boards[i].copy()
            prev_winning_boards.append(i)


if winning_board != None:
    print(f'Last winning board is: {winning_board}; and the winning number is: {winning_number}')

# Calculate score for winning board

sum_num = 0

for i in range(len(winning_board_state)):

    if winning_board_state[i] != 'X':
        sum_num += int(winning_board_state[i])

print(f'Winning score is: {sum_num * int(winning_number)}')