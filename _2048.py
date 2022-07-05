import numpy as np
import random


def show(GRID):
    print(GRID)


def init(GRID):
    # Places two numbers on the board
    insertNumber(GRID)
    insertNumber(GRID)
    show(GRID)
    print("init")


def insertNumber(GRID):
    # Grabs the indexes of every 0, chooses a random one, then changes the index to either 2 or 4
    item = random.choice(np.argwhere(GRID == 0)) # try catch block for when the user looses
    GRID[item[0], item[1]] = random.choice([2,4])


def isLegal():
    pass


def left(GRID):
    for i in range(4):
        x = GRID[i] # Grab i'th row
        x = x[x != 0] # Remove the 0's
        n = x.size-1
        j = 0
        while j < n:
            if x[j] == x[j+1]:
                x[j] = x[j]*2
                x[j+1] = 0 
                j += 1
            j += 1

        x = x[x != 0]
        x = np.pad(x, (0,4-len(x))) # Pad so that len is 4
        GRID[i] = x


def right(GRID):
    for i in range(4):
        x = GRID[i][::-1] # Grab the reverse of i'th row
        x = x[x != 0]
        n = x.size-1
        j = 0
        while j < n:
            if x[j] == x[j+1]:
                x[j] = x[j]*2
                x[j+1] = 0 
                j += 1
            j += 1

        x = x[x != 0]
        x = np.pad(x, (0,4-len(x)))
        GRID[i] = x[::-1]


def up(GRID):
    for i in range(4):
        x = GRID[:, i] # Grab the i'th column
        x = x[x != 0]
        n = x.size-1
        j = 0
        while j < n:
            if x[j] == x[j+1]:
                x[j] = x[j]*2
                x[j+1] = 0 
                j += 1
            j += 1

        x = x[x != 0]
        x = np.pad(x, (0,4-len(x)))
        GRID[:, i] = x


def down(GRID):
    for i in range(4):
        x = GRID[:, i][::-1] # Grab the reverse of the i'th column 
        x = x[x != 0]
        n = x.size-1
        j = 0
        while j < n:
            if x[j] == x[j+1]:
                x[j] = x[j]*2
                x[j+1] = 0 
                j += 1
            j += 1

        x = x[x != 0]
        x = np.pad(x, (0,4-len(x)))
        GRID[:, i] = x[::-1]


def evaluate(TEMPLATE, GRID):
    print(np.multiply(TEMPLATE, GRID).sum())

