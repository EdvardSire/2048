import numpy as np
from _2048 import *

TEMPLATE = np.array([[0.135,  0.121,  0.102,  0.0999],
                     [0.0997, 0.088,  0.076,  0.0724],
                     [0.0606, 0.0562, 0.0371, 0.0161],
                     [0.0125, 0.0099, 0.0057, 0.0033]], dtype=np.float64)

GRID = np.zeros((4,4), dtype=np.uint16)

gameFinished = False

###

def game():
    init(GRID)

    while not(gameFinished):
        show(GRID)
        try:
            key = str(input())
            if key == 'w':
                up(GRID)
            if key == 'a':
                left(GRID)
            if key == 's':
                down(GRID)
            if key == 'd':
                right(GRID)
            if key == 'f':
                evaluate(TEMPLATE, GRID)

        except IllegalMove:
            print("Illegal Move")

        else:
            try:
                insertNumber(GRID)
            except:
                gameFinished = not(gameFinished)


    print("Done")
    print(evaluate(TEMPLATE, GRID))


def updateBest():
    bestGRID = np.copy(iterGRID)


l = [left, right, up, down]
sequence = ""


def nMovesDeep(GRID, iterGRID, bestGRID):
    #print("GRID", evaluate(TEMPLATE, GRID))
    #print("iterGRID", evaluate(TEMPLATE, iterGRID))
    #print("bestGRID", evaluate(TEMPLATE, bestGRID))

    for i in range(4):
        print(l[i](iterGRID))
        if evaluate(TEMPLATE, l[i](iterGRID)) > evaluate(TEMPLATE, bestGRID):
            np.copyto(bestGRID, l[i](iterGRID))
            print("hit")
    print(bestGRID)






init(GRID)
show(GRID)

bestGRID = np.copy(GRID)
iterGRID = np.copy(GRID)

nMovesDeep(GRID, iterGRID, bestGRID)

