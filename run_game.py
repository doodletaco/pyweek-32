###
### Author: doodleTaco
### Description: My entry to Pyweek 32.
###              A card-matching game, centered around escaping a dream.
###

import random
# import pygame (not needed yet)


def create_board(size):
    '''
    This initializes the cards to be matched.
    size: Can be any integer that is at least 1.
    '''
    pairs = (size * (size + 1)) // 2

    # create string with list of pairs
    board_string = ''
    for i in range(pairs):
        board_string += str(i) * 2

    # shuffle string
    board_string = ''.join(random.sample(board_string, len(board_string)))

    # convert string into array
    index = 0
    board_list = []
    for i in range(size):
        row = []
        for j in range(size + 1):
            row.append(board_string[index])
            index += 1
        board_list.append(row)

    return board_list


# accept user input

# check if matching

# update board

# print board in readable way
def print_board(board):
    '''
    This function prints the board in a way readable to humans.
    board: Can be any 2D List.
    '''
    # TODO:
    length = len(board[0])
    top = '  │ '
    for i in range(length):
        top += str(i + 1) + ' '
    print(top)
    print('──┼' + '─' * length * 2)
    for index, row in enumerate(board):
        thing = str(index + 1) + ' │ '
        for column in row:
            thing += column + ' '
        print(thing)

# game loop
print_board(create_board(3)) # testing if table creation works
