import sys

inputFile = open(sys.argv[1], "r")
outputFile = open(sys.argv[2], "w+")

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

def checkBoard(b):
    for clique in Cliques:
        temp = list()
        for index in clique:
            if(b[index] == "_"):
                return False
            temp.append(b[index])
        for index in clique:
            temp.remove(b[index])
            if(b[index] in temp):
                return False
    return True

def calculatePossibilities(b):
    possibilities = list()
    for x in range(81):
        possibilities.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for x in range(81):
        for clique in Cliques:
            if(x in clique and b[x] == "_"):
                cliqueValues = list()
                for index in clique:
                    if(b[index] != "_"):
                        cliqueValues.append(int(b[index]))
                # print(cliqueValues)
                for value in cliqueValues:
                    if(value in possibilities[x]):
                        possibilities[x].remove(value)
    return possibilities

boardsInFile = loadBoards()
boardToSolve = boardsInFile[sys.argv[3]]

boardStack = list()
boardStack.append(boardToSolve[:])
currentBoard = boardToSolve[:]

possibilitiesStack = list()
possibilitiesStack.append(calculatePossibilities(currentBoard))
currentPossibilties = calculatePossibilities(currentBoard)

# print(currentPossibilties)
# exit()
while not checkBoard(currentBoard):
    counter = 0
    print(boardToString(currentBoard))
    print(currentPossibilties)
    while(counter < 81 and currentBoard[counter] != "_" and len(currentPossibilties[counter]) == 0):
        counter += 1
    if(counter >= 81):
        print('bruh')
        currentBoard = boardStack.pop()
        currentPossibilties = possibilitiesStack.pop()
    else:
        if(len(currentPossibilties[counter]) > 0 and currentBoard[counter] == "_"):
            print("okay")
            currentBoard[counter] = currentPossibilties[counter].pop()
            boardStack.append(list.copy(currentBoard))
            possibilitiesStack.append(calculatePossibilities(currentBoard))

# def solve():
#     global currentBoard
#     global currentPossibilties
#     global boardStack
#     global possibilitiesStack
#     counter = 0
#     print(boardToString(currentBoard))
#     while(currentBoard[counter] == "_" and counter < 81):
#         counter += 1
#     if(counter < 81):
#         if(len(currentPossibilties[counter]) == 0 and len(boardStack) > 1):
#             currentBoard = boardStack.pop()
#             currentPossibilties = possibilitiesStack.pop()
#             solve()
#         elif(len(currentPossibilties[counter]) > 0):
#             currentBoard[counter] = currentPossibilties[counter].pop()
#             boardStack.append(list.copy(currentBoard))
#             possibilitiesStack.append(calculatePossibilities(currentBoard))
#             solve()

# solve()

outputFile.write(boardToString(currentBoard))