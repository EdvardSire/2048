'''This module has a function to insert a random number into a 2048 grid'''
from random import choice
from numpy import multiply, argwhere


def init(iterGRID):
    insertRandomNumber(iterGRID)
    insertRandomNumber(iterGRID)
    print("init")
    show(iterGRID)
    print("")


def show(sGRID):
    print(sGRID)


def evaluate(template, mulGRID):
    return multiply(template, mulGRID).sum()


def insertRandomNumber(GRID):
    # Grabs the indexes of every 0, chooses a random pair, then changes the index to either 2 or 4
    # try catch block for when the user looses
    item = choice(argwhere(GRID == 0))
    GRID[item[0], item[1]] = choice([2, 4])
