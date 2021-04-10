from numpy import *
sudokuBoard = [
[0,0,0,7,3,4,0,0,0],
[9,3,0,5,0,6,7,0,2],
[5,7,4,9,0,8,1,6,3],
[0,5,3,1,4,0,0,9,7],
[0,0,0,0,0,0,0,3,1],
[6,1,7,8,9,3,0,0,4],
[0,4,6,2,8,1,9,0,5],
[0,9,0,4,6,0,3,2,8],
[2,8,0,0,7,9,0,0,6]
]
print('The Sudoku board you entered: ')
for i in range(9):
    for j in range(9):
        print("|" + str(sudokuBoard[i][j]) + "|" ,end=" ")
    print("\n|---------------------------------|")
def squareIsValid(board,y,x,n):
    #search horizontally
    for i in range(9):
        if board[y][i] == n:
            return False
    #search vertically
    for i in range(9):
        if board[i][x] == n:
            return False
    #chose a square and search in the square
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[y0 + i][x0 + j] == n:
                return False
    return True


def solveTheBoard(board):
    #checking if the lil square is empty or not
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                #if its empty check all the possibilities
                for n in range(1,10):
                    if squareIsValid(board,y,x,n):
                        board[y][x] = n
                        #checking if this possibility works for the other squares
                        #if its not make it empty again
                        solveTheBoard(board)
                        board[y][x] = 0
                return
    print("The Solution :")
    for i in range(9):
        for j in range(9):
            print("|" + str(sudokuBoard[i][j]) + "|" ,end=" ")
        print("\n|---------------------------------|")
    input('do you wanna check is there another solution?')

solveTheBoard(sudokuBoard)