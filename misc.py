'''This module inserts random numbers, evaluates and shows prints a 2048 grid'''
from random import choice
from numpy import multiply, argwhere


def init(GRID):
    '''Initializes the board with two numbers'''
    insertRandomNumber(GRID)
    insertRandomNumber(GRID)


def show(GRID):
    '''Prints the grid'''
    print(GRID)


def evaluate(template, mulGRID):
    '''Returns a float representing the "score" of a boardstate, higher is better'''
    return multiply(template, mulGRID).sum()


def insertRandomNumber(GRID):
    '''Inserts 2 or 4 randomly into an *empty* cell'''
    # Grabs the indexes of every 0, chooses a random pair, then changes the index to either 2 or 4
    item = choice(argwhere(GRID == 0))
    GRID[item[0], item[1]] = choice([2, 4])
