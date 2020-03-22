#! /usr/bin/python3

import sys

backtracks = 0

def main(args = list()):

    if(len(args) == 0):
        args = sys.argv[:]

    inputFile = open(args[1], "r")
    outputFile = open(args[2], "w+")

    Cliques=[[0,1,2,3,4,5,6,7,8],\
    [9,10,11,12,13,14,15,16,17],\
    [18,19,20,21,22,23,24,25,26],\
    [27,28,29,30,31,32,33,34,35],\
    [36,37,38,39,40,41,42,43,44],\
    [45,46,47,48,49,50,51,52,53],\
    [54,55,56,57,58,59,60,61,62],\
    [63,64,65,66,67,68,69,70,71],\
    [72,73,74,75,76,77,78,79,80],\
    [0,9,18,27,36,45,54,63,72],\
    [1,10,19,28,37,46,55,64,73],\
    [2,11,20,29,38,47,56,65,74],\
    [3,12,21,30,39,48,57,66,75],\
    [4,13,22,31,40,49,58,67,76],\
    [5,14,23,32,41,50,59,68,77],\
    [6,15,24,33,42,51,60,69,78],\
    [7,16,25,34,43,52,61,70,79],\
    [8,17,26,35,44,53,62,71,80],\
    [0,1,2,9,10,11,18,19,20],\
    [3,4,5,12,13,14,21,22,23],\
    [6,7,8,15,16,17,24,25,26],\
    [27,28,29,36,37,38,45,46,47],\
    [30,31,32,39,40,41,48,49,50],\
    [33,34,35,42,43,44,51,52,53],\
    [54,55,56,63,64,65,72,73,74],\
    [57,58,59,66,67,68,75,76,77],\
    [60,61,62,69,70,71,78,79,80]\
    ]

    def boardToString(board):
        counter = 1
        output = ""
        for x in board:
            if(counter % 9 == 0):
                output = output + str(x) + "\n"
            else:
                output = output + str(x) + ","
            counter += 1
        return output

    def loadBoards():
        boards = dict()
        board = list()
        rowsRead = 0
        for line in inputFile:
            lineArray = line.strip().split(",")
            # print(lineArray)
            if(len(lineArray) == 3):
                title = lineArray[0]
            if(len(lineArray) == 9):
                rowsRead += 1
                board.extend(lineArray)
            if(rowsRead == 9):
                rowsRead = 0
                boards[title] = board
                board = list()
        return boards

    def calculatePossibilities(b):
        possibilities = list()
        for x in range(81):
            possibilities.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
        for x in range(81):
            for clique in Cliques:
                if(b[x] != "_"):
                    possibilities[x] = list()
                if(x in clique):
                    cliqueValues = list()
                    for index in clique:
                        if(b[index] != "_"):
                            cliqueValues.append(int(b[index]))
                    for value in cliqueValues:
                        if(value in possibilities[x]):
                            possibilities[x].remove(value)
        return possibilities

    boardsInFile = loadBoards()
    boardToSolve = boardsInFile[args[3]]

    boardStack = list()
    currentBoard = list.copy(boardToSolve)

    def solve(currentBoard, index):
        global backtracks
        if(currentBoard[index] == "_"):
            currentPossibilities = calculatePossibilities(currentBoard)
            # Iterate through all possible values
            for x in currentPossibilities[index]:
                # Replace the value of the current square
                currentBoard[index] = x
                # If we are at the last position, return True
                if(index == 80):
                    return True
                # If the next index also returns true, return True
                if(solve(currentBoard, index + 1)):
                    return True
            # If after iterating through all possibilities, no solution is reached, return False
            currentBoard[index] = "_"
            backtracks += 1
            return False
        else:
            # If the value of the current square is already set, return the value of the next square
            return solve(currentBoard, index + 1)

    solve(currentBoard, 0)

    print(backtracks)

    outputFile.write(boardToString(currentBoard))

main()

# main("A1-1")
# main("A2-1")
# main("A3-1")
