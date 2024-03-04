# import(s)
from random import choice
from keyboard import is_pressed
from time import sleep



# funcs for logic

# displaying board
def Display(board=dict, boardRows=list):
    print(board[boardRows[0]])
    print(board[boardRows[1]])
    print(board[boardRows[2]])
    print(board[boardRows[3]])

# moving the board
def shiftBoard(board=dict, boardRows=list, spawnablenums=list, key=str):

    canmovetospace = [0,0,0,0]
    
    if key == "left":
        print("left")
        
                

    # logic to display board
    Display(board, boardRows)

    sleep(.25)