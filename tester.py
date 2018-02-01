from Board import Board
from Move import Move

test_board = Board(15, 15)
test_board.printBoard(['goneo', 'gomokuneo'])

move = Move('goneo', 12, 0)
print(test_board.inBoard((move.x, move.y)))