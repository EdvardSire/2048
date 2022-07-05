import numpy as np
from _2048 import *

TEMPLATE = np.array([[0.135,  0.121,  0.102,  0.0999],
                     [0.0997, 0.088,  0.076,  0.0724],
                     [0.0606, 0.0562, 0.0371, 0.0161],
                     [0.0125, 0.0099, 0.0057, 0.0033]], dtype=np.float64)

GRID = np.zeros((4,4), dtype=np.uint16)

###

init(GRID)

while True:
    key = str(input())
    if key == 'w':
        up(GRID)
        insertNumber(GRID)
        show(GRID)
    if key == 'a':
        left(GRID)
        insertNumber(GRID)
        show(GRID)
    if key == 's':
        down(GRID)
        insertNumber(GRID)
        show(GRID)
    if key == 'd':
        right(GRID)
        insertNumber(GRID)
        show(GRID)
    if key == 'f':
        evaluate(TEMPLATE, GRID)

