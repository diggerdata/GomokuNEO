class Move:
    def __init__(self, team=None, x=-1, y=-1):
        self.team = team
        self.x = x
        self.y = y
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]

    def __str__(self):
        
        print("Y move: " + str(self.y))
        return "%s %s %s" % (self.team, self.letters[self.x], (self.y+1))


    def parseMove(self, move):
        """
        move: string

        move is of the format the referee expects: 'team column(x) row(y)'
        """
        items = move.split(' ') #split by spaces
        self.team = items[0]
        self.x = self.letters.index(items[1].lower())
        self.y = int(items[2]) - 1

        return self