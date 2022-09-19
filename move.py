'''This module has functions to move a 2048 grid right, left, up and down'''
import numpy as np
from vars import ROWS
from misc import insertRandomNumber


class IllegalMove(Exception):
    pass




def move(direction, GRID):
    tryGRID = np.copy(GRID)
    for i in range(ROWS):
        match direction:
            case "up":
                x = tryGRID[:, i]  # Grab the i'th column
                x = x[x != 0]  # Remove the 0's
            case "down":
                x = tryGRID[:, i][::-1]  # Grab the reverse of the i'th column
                x = x[x != 0]  # Remove the 0's
            case "left":
                x = tryGRID[i]  # Grab i'th row
                x = x[x != 0]  # Remove the 0's
            case "right":
                x = tryGRID[i][::-1]  # Grab i'th row reversed
                x = x[x != 0]  # Remove the 0's
        n = x.size-1 
        j = 0

        while j < n:
            if x[j] == x[j+1]:
                x[j] = x[j]*2
                x[j+1] = 0
                j += 1
            j += 1

        x = x[x != 0]
        x = np.pad(x, (0, ROWS-len(x)))  # Pad so that len is 4
        match direction:
            case "up":
                tryGRID[:, i] = x
            case "down":
                tryGRID[:, i] = x[::-1]
            case "left":
                tryGRID[i] = x
            case "right":
                tryGRID[i] = x[::-1]
    if np.array_equal(tryGRID, GRID) is True:
        raise IllegalMove("error")
    else:
        # np.copyto(GRID, tryGRID) # for the game
        insertRandomNumber(tryGRID)
        return tryGRID

