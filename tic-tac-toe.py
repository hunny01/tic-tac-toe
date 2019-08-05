#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def createBoard():
    board = np.zeros((3, 3), dtype = 'str')
    return board

def addValueToBoard(board, position, val):
    if position < 4:
        board[0][position-1] = val
        return board
    if position > 3 and position < 7:
        board[1][position-4] = val
        return board
    if position > 6:
        board[2][position-7] = val
        return board

def validateInput(board, position):
    if position < 4:
        if board[0][position-1] != '':
            return False
    if position > 3 and position < 7:
        if board[1][position-4] != '':
            return False
    if position > 6:
        if board[2][position-7] != '':
            return False

def checkGameOver(board):
    # Check For Draw !!
    if len(np.where(board == 0)[0]) != '':
        return False
    return True

def winningMove(board, val):
    winner = False
    
    # Check For Horizontal Line
    if board[0][0] == val and board[0][1] == val and board[0][2] == val:
        winner = True
    if board[1][0] == val and board[1][1] == val and board[1][2] == val:
        winner = True
    if board[2][0] == val and board[2][1] == val and board[2][2] == val:
        winner = True
    
    # Check For Vertical Line
    if board[0][0] == val and board[1][0] == val and board[2][0] == val:
        winner = True
    if board[0][1] == val and board[1][1] == val and board[2][1] == val:
        winner = True
    if board[0][2] == val and board[1][2] == val and board[2][2] == val:
        winner = True

    # Check For Diagonal Line
    if board[0][0] == val and board[1][1] == val and board[2][2] == val:
        winner = True
    if board[0][2] == val and board[1][1] == val and board[2][0] == val:
        winner = True
    
    return winner
        
board = createBoard()
print(board)

counter = 0
while True:

    # Taking User Input
    counter = counter%2
    counter += 1
    if counter == 1:
        while True:
            # User 1 Input
            position = input(f'\nPlayer 1 (\'X\') Please Select A Position From (1-9): ')
            if position.isnumeric() != 1:
                print('Wrong Input, Please Enter A Number Between (1-9), You Enetered A String')
                continue
            else:
                position = int(position)
            if position > 9:
                print('Wrong Input, Please Enter Between (1-9) Only')
                continue
            if validateInput(board, position) == False:
                print('Wrong Input, This Position Is Already Filled. Please Select Any Other Position')
                continue
            break
        val = 'X'
    else:
        while True:
            # User 2 Input
            position = input(f'\nPlayer 2 (\'O\') Please Select A Position From (1-9): ')
            if position.isnumeric() != 1:
                print('Wrong Input, Please Enter A Number Between (1-9), You Enetered A String')
                continue
            else:
                position = int(position)
            if position > 9:
                print('Wrong Input, Please Enter Between (1-9) Only')
                continue
            if validateInput(board, position) == False:
                print('Wrong Input, This Position Is Already Filled. Please Select Any Other Position')
                continue
            break
        val = 'O'

    # Printing The Board After User Input
    print(addValueToBoard(board, position, val))
    
    # Check If Any One Of The Two Player Wins The Game
    if winningMove(board, val) == True:
        if val == 'X':
            print('\nCongratulations !! Player 1 Wins !!')
        else:
            print('\nCongratulations !! Player 2 Wins !!')
        break

    # Checking If Game Is A Draw
    if checkGameOver(board) == True:
        print(f'Nobody Wins !! Its A Draw')
        break

