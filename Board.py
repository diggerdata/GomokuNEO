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


    def __init__(self, width, height):
        """
        defines the board width the given width and height
        """
        self.board = [[self._Cell() for x in range(width)] for x in range(height)]
        self.width = width
        self.height = height
        self.move_history = []


    def __str__(self):
        string = ""
        if self.win:
            string += self.winstatement +"\n"
        string+="  "
        for i in range(self.size):
            string+="{0}{1}".format(i%10, " " if i<10 else "'")
        string +="\n"
        i = 0
        for x in self.board:
            string +="{0}{1}".format(i%10," " if i<10 else "'")
            i+=1
            for y in x:
                string+="{0} ".format(y)
            string+="\n"
        return string

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
        print ("")
        print ('{0} -- {1}'.format('X', teams[0]))
        print ('{0} -- {1}'.format('O', teams[1]))
        print ("")
        sys.stdout.write("   ")
        for x in range(self.width):
            sys.stdout.write('%s ' % (chr(x+ord('A'))))
        sys.stdout.write("\n")
        for y in range(self.height):
            sys.stdout.write('%02s ' % (y+1))
            for x in range(self.width):
                if self.board[x][y].team is None:
                    sys.stdout.write('-')
                else:
                    #team_name_hash = hashlib.md5(self._field[x][y].team).hexdigest()
                    if teams.index(self._field[x][y].team) == 0:
                        team_color = 'X'
                    else:
                        team_color = 'O'
                    sys.stdout.write(team_color)
                sys.stdout.write(' ')
            sys.stdout.write('\n')
            
        sys.stdout.flush()

    def getEmptyFields(self):
        return [[(x, y) for x in range(self.width)]
                        for y in range(self.height)
                        if self.isFieldOpen((x, y))]
       

class color:
    """
    A simple color class.
    Initializes with a bool argument:
    Arbitrarily, True->color is black
                 False->color is white
    """
    def __init__(self, isBlack):
        if isBlack:
            self.isBlack = True
            self.color = "BLACK"
            self.symbol = "x"
        else:
            self.isBlack = False
            self.color = "WHITE"
            self.symbol = "o"

    def __eq__(self, other):
        return type(self)==type(other) and \
           self.color==other.color

    def __ne__(self,other): return not (self == other)

    def __str__(self): return self.color

    def __repr__(self): return str(self)

    def swap(self): #swaps a color object from Black->White or reverse
        self.__init__(not self.isBlack)

    def getNot(self): #returns a color object != self
        return color(not self.isBlack)