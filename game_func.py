import os
import random

# keep screen clear to one single display
def clear():
    os.system( 'cls' )

# Building the board, This builds the graphics and enumerate the positons of the board,
# it defines a functions which expects an input for each position in the board.  
def display_board(board):
    
    clear()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# This function ask the player weather it wants to be X or 0, it basically keeps asking the player the same
# question until the player gives it a valid answer either through a capitalize letter or not.
def player_input():
    
    marker = ''
    while not(marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


# This function takes the board, either 0 or X chosen by player, and sets
# that mark at the specified location
def place_marker(board, marker, position):
    board[position] = marker


# The fuction defines the different way a player can win, if a given mark exist or is true
# in any of these condition, than it is consider a win.
def win_check(board,mark):

     return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# Draw to see what player will go first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# This fucntion checks weather a certain space on the board is empty or not
# it will return either a True or False Statement
def space_check(board, position):
    
    return board[position] == ' '


# Check available spaces
# If there is empty space in the game in spaces 1-9 return False(The board is not full), else if 
# there is not empty spaces than return True(The board is in fact full)
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# This function keeps asking the player to choose its next desire position
def player_choice(board):
    position = ' '
    
    # while a given input is not any of the numbers 1-9 or
    # weather a space in the board is empty or already taken
    # it keeps asking the questions until one or the other becomes a false statement
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        position = input('Choose your next position: (1-9) ')
    return int(position)


# define function to ask player weather they want to play again or not.
def replay():
    
    return input('Do you want to play again? Enter Yes or No:  ').lower().startswith('y')
