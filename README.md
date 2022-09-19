# Inspiration
https://medium.com/geekculture/2048-ai-python-highest-score-cc143b55994c

https://cs229.stanford.edu/proj2016/report/NieHouAn-AIPlays2048-report.pdf

# Starting point
The whole project started with this heuristic for evaluating a board started
IMAGE OF TEMPLATE
def evalgrid(grid):
    return np.sum(np.array(grid) * TEMPLATE)TEMPLATE = [[0.135, 0.121, 0.102, 0.0999],
            [0.0997, 0.088, 0.076, 0.0724],
            [0.0606, 0.0562, 0.0371, 0.0161],
            [0.0125, 0.0099, 0.0057, 0.0033]]

# Dependencies
Python 3.10.6 and numpy 1.23.3
