import numpy as np
import timeit
from move import move
from misc import init, show, evaluate
from vars import TEMPLATE, MAX_DEPTH, ROWS


l = ["left", "right", "up", "down"]


def deep(n=0):
    global depth
    global iterGRID
    localGRID = np.copy(iterGRID)

    for i in range(4):  # Loops over all moves, and those moves loops over moves
        try:
            iterGRID = move(l[i], localGRID)  # Are there any legal moves

        except:
            continue  # Go to next move

        else:  # No exception
            if evaluate(TEMPLATE, iterGRID) > evaluate(TEMPLATE, bestGRID):
                np.copyto(bestGRID, iterGRID)
            if MAX_DEPTH > n:
                deep(n+1)

    return


# START
average = []
for i in range(1):
    start = timeit.default_timer()
    iterGRID = np.zeros((ROWS, ROWS), dtype=np.uint16)
    init(iterGRID)
    show(iterGRID)
    bestGRID = np.copy(iterGRID)

    for i in range(10):
        deep()
    iterGRID = np.copy(bestGRID)

    print(bestGRID)
    print('Time: ', timeit.default_timer()-start)
    average.append(timeit.default_timer()-start)

print(average)
