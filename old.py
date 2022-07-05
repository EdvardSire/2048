import random
import numpy as np

TEMPLATE = [[0.135,  0.121,  0.102,  0.0999],
            [0.0997, 0.088,  0.076,  0.0724],
            [0.0606, 0.0562, 0.0371, 0.0161],
            [0.0125, 0.0099, 0.0057, 0.0033]]

GRID = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]



def getZeroSquares():
    values = []
    with np.nditer(np.array(GRID), flags=['multi_index']) as it:
        for x in it:
            if x == 0:
                values.append(it.multi_index)
    return values


def show():
    print(np.array(GRID))


def update():
    square = random.choice(getZeroSquares())
    #print(square)
    GRID[square[0]][square[1]] = random.choice([2, 4])
    show()
    

def initialize():
    update()
    update()



def move(direction):
    if(direction == "left" or "right"):
        for j in range(4):
            if(direction == "right"): GRID[j] = GRID[j][::-1]
            for i in range(GRID[j].count(0)):
                GRID[j].append(GRID[j].pop(GRID[j].index(0)))
            for i in range(3-GRID[j].count(0)):
                if(GRID[j][i] == GRID[j][i+1]):
                    GRID[j][i] = GRID[j][i]*2
                    GRID[j][i+1] = 0
                    GRID[j].append(GRID[j].pop(i+1))
            if(direction == "right"): GRID[j] = GRID[j][::-1]
    else:
        pass

    show()


initialize()
print("start")

for i in range(20):
    print("move:")
    move("right")
    print("update:")
    update()
