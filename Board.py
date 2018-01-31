import copy
import sys

class Board:
    """
    A class that defines the board
    for a game of gomoku
    """

    class _Cell:
        """
        A class that defines a single cell on the board. Initialized to empty cell
        """
        isEmpty = True
        team = None

        def playField(self, team):
            self.isEmpty = False
            self.team = team


    def __init__(self, width=15, height=15):
        """
        defines the board width the given width and height
        """
        self.board = [[self._Cell() for x in range(width)] for x in range(height)]
        self.width = width
        self.height = height
        self.move_history = []


    def __str__(self):
        pass
            

    def __getitem__(self, coords):
        (x, y) = coords
        return self.board[x][y]

    def __eq__(self,other):
        return ( 
        type(self) == type(other) and 
        self.width  == other.width and 
        self.height == other.height)

    def placeToken(self, move):
        self.move_history.append(move)
        return self.board[move.x][move.y].playField(move.team)

    def inBoard(self, coords):
        """
        (coords) : (int,int)
        return: bool
        
        Takes a set of coordinates, and returns True if
        it represents a valid space on the board
        Else, False
        """
        (x, y) = coords
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def isFieldOpen(self, coords):
        (x, y) = coords
        return self.inBoard(coords) and self.board[x][y].isEmpty()

    def isFull(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.isFieldOpen((x, y)):
                    return False
        return True # if no empty cells found

    def printBoard(self, teams):
        output = ''
        output += '{0} -- {1}\n'.format('X', teams[0])
        output += '{0} -- {1}'.format('O', teams[1])
        output += '\n   '
        for x in range(self.width):
            output += '{0} '.format(chr(x+ord('A')))
        output += "\n"
        for y in range(self.height):
            output += '{0:2d} '.format(y+1)
            for x in range(self.width):
                if self.board[x][y].team is None:
                    output += '-'
                else:
                    if teams.index(self._field[x][y].team) == 0:
                        team_color = 'X'
                    else:
                        team_color = 'O'
                    output += team_color
                output += ' '
            output += '\n'
        print(output)
        

    def getEmptyFields(self):
        return [[(x, y) for x in range(self.width)]
                        for y in range(self.height)
                        if self.isFieldOpen((x, y))]