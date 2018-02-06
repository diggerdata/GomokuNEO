from Broad import Broad
from Move import Move
import numpy as np
import numpy.ma as ma


def run():
    board = Broad(['goneo', 'gomokuneo'], 5, 5)
    move = Move('goneo', 1, 1)
    board.placeToken(move)
    board.printBoard()
    horizontalRun(board)


def horizontalRun(board):
    row = 0
    while row < board.height:
        col = 0
        while col < board.width - 4:
            a = np.ones(shape=(board.width, board.height))
            print('row: {0}, col: {1}'.format(row, col))
            a[row:row+1, col:col+5] = 0
            mx = ma.masked_array(board.board, mask=a)
            validWindow(mx.compressed())
            # print(a)
            col += 1

        row += 1


def validWindow(array):
    enemy = Broad.Cell(False, 'gomokuneo')

    if enemy in array:
        print('enemy cell')
        return False

    if not enemy in array:
        print('no enemy cell')

    for x in array:
        print(x)

run()
