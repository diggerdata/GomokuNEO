import time
import logging
import Move
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

group_file = '.\gomokuneo.go'
end_file = '.\end_game'
group_file_exists = False

def start(): 
    pass
    watch_directory()
    while(True):
        if group_file_exists:
            if(check_file_exists(end_file)): # first check if end game file exists too
                break # game over
            else:
                opp_move = #read move file
                next_move()

def check_file_exists(self, path):
    file = Path(path)
    return file.is_file()


class Game:
    def __init__(self, width, height, length_to_win):
        self.turn = 0
        self.board = Board(width, height)
        self.length_to_win = length_to_win
        

    def isValidMove(self, move):
        """
        move: Move
        return: bool

        Takes a Move object, and returns True if
        the move is valid and can be made.
        Else, False
        """
        if self.turn == 1:
            return self.isMoveOnBoard(move)
        else:
            return self.isMoveOnBoard(coords) and self.isMoveUnique.board, coords)


    def isMoveUnique(self, move):
        return self.board.isFieldOpen((move.x, move.y))

    def isMoveOnBoard(self, move):
        return self.board.inBoard((move.x, move.y))

    def makeMove(self, move):
        if self.isValidMove(move):
            self.board.placeToken(move)
            self.turn += 1
            return True
        else:
            return False


