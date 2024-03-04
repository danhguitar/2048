from engine import *

def main():

    spawnNums = [2,4]

    GameBoard = {
        "rowA": [1,0,0,0],
        "rowB": [0,1,0,0],
        "rowC": [0,0,1,0],
        "rowD": [0,0,0,1]
    }
    
    BoardRows = [
        "rowA",
        "rowB",
        "rowC",
        "rowD"
    ]
    
    #(GameBoard, BoardRows, spawnNums)
    #with keyboard.Listener(on_release=shiftBoard) as keyBoardIn:

        #while True:
            #keyBoardIn.join()
    
    while True:
        if is_pressed('left'):
            shiftBoard(GameBoard, BoardRows, spawnNums, "left")



if __name__ == "__main__":
    main()