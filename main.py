import numpy as np
import random
import timeit

TEMPLATE = np.array([[0.135,  0.121,  0.102,  0.0999],
                     [0.0997, 0.088,  0.076,  0.0724],
                     [0.0606, 0.0562, 0.0371, 0.0161],
                     [0.0125, 0.0099, 0.0057, 0.0033]], dtype=np.float64)

# TEMPLATE2 = np.array([[0.135, 0.121],
#                       [0.102, 0.099]], dtype=np.float64)

# TEMPLATE3 = np.array([[0.135,  0.121,  0.102],
#                       [0.0999, 0.0997, 0.088],
#                       [0.076, 0.0724, 0.0606]], dtype=np.float64)

ROWS = 4
MAX_DEPTH = 6


def show(sGRID):
    print(sGRID)


def init():
    # Places two numbers on the board
    insertNumber(iterGRID)
    insertNumber(iterGRID)
    print("init")
    show(iterGRID)
    print("")


def insertNumber(GRID):
    # Grabs the indexes of every 0, chooses a random pair, then changes the index to either 2 or 4
    item = random.choice(np.argwhere(GRID == 0)) # try catch block for when the user looses
    GRID[item[0], item[1]] = random.choice([2,4])


class IllegalMove(Exception):
    pass


def left(GRID):
    tryGRID = np.copy(GRID)
    for i in range(ROWS):
        x = tryGRID[i] # Grab i'th row
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
        x = np.pad(x, (0,ROWS-len(x))) # Pad so that len is 4
        tryGRID[i] = x

    if np.array_equal(tryGRID, GRID) is True:
        raise IllegalMove("error")
    else:
       #np.copyto(GRID, tryGRID) # for the game
       insertNumber(tryGRID)
       return tryGRID


def right(GRID):
    tryGRID = np.copy(GRID)
    for i in range(ROWS):
        x = tryGRID[i][::-1] # Grab i'th row reversed
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
        x = np.pad(x, (0,ROWS-len(x))) # Pad so that len is 4
        tryGRID[i] = x[::-1]

    if np.array_equal(tryGRID, GRID) is True:
        raise IllegalMove("error")
    else:
       #np.copyto(GRID, tryGRID) # for the game
       insertNumber(tryGRID)
       return tryGRID


def up(GRID):
    tryGRID = np.copy(GRID)
    for i in range(ROWS):
        x = tryGRID[:, i] # Grab the i'th column
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
        x = np.pad(x, (0,ROWS-len(x))) # Pad so that len is 4
        tryGRID[:, i] = x

    if np.array_equal(tryGRID, GRID) is True:
        raise IllegalMove("error")
    else:
       #np.copyto(GRID, tryGRID) # for the game
       insertNumber(tryGRID)
       return tryGRID


def down(GRID):
    tryGRID = np.copy(GRID)
    for i in range(ROWS):
        x = tryGRID[:, i][::-1] # Grab the reverse of the i'th column
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
        x = np.pad(x, (0,ROWS-len(x))) # Pad so that len is 4
        tryGRID[:, i] = x[::-1]

    if np.array_equal(tryGRID, GRID) is True:
        raise IllegalMove("error")
    else:
       #np.copyto(GRID, tryGRID) # for the game
       insertNumber(tryGRID)
       return tryGRID


def evaluate(template, mulGRID):
    return np.multiply(template, mulGRID).sum()



l = [left, right, up, down]
ln = ["left", "right", "up", "down"]

def deep(n=0):
    global depth
    global iterGRID
    localGRID = np.copy(iterGRID)

    for i in range(4):
        try:
            iterGRID = l[i](localGRID) # Are there any legal moves
            #print(n)
            #print(ln[i])
            #print(iterGRID)

        except:
            #print("fail")
            continue

        else:
            if evaluate(TEMPLATE, iterGRID) > evaluate(TEMPLATE, bestGRID):
                np.copyto(bestGRID, iterGRID)
            if MAX_DEPTH > n:
                deep(n+1)

    return


### START
average = []
for i in range(10):
    start = timeit.default_timer()
    iterGRID = np.zeros((ROWS,ROWS), dtype=np.uint16)
    init()
    bestGRID = np.copy(iterGRID)

    for i in range(10):
        deep()
    iterGRID = np.copy(bestGRID)

    print(bestGRID)
    print('Time: ', timeit.default_timer()-start)
    average.append(timeit.default_timer()-start)

print(average)

