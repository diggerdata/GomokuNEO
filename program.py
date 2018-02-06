import sys
import time
import Move
from Board import Board
from Player import Player

end_file = '.\end_game'

def check_file_exists(self, path):
    file = Path(path)
    return file.is_file()


class Game:
    def __init__(self, width = 15, height = 15, length_to_win = 5):
        self.turn = 0
        self.board = Board(width, height)
        self.length_to_win = length_to_win
        

    def getBoard(self):
        return self.board

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
            return self.isMoveOnBoard(coords) and self.isMoveUnique(coords)


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

    def start(self, team_name): 
        player1 = Player(self, team_name)
        player1.maxdepth=1


def main():
    if sys.argv[1] != None:
        team_name = sys.argv[1]
        game = Game()
        game.start(team_name)

main()


