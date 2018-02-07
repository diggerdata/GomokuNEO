class Move:
    def __init__(self, team=None, x=-1, y=-1):
        self.team = team
        self.x = x
        self.y = y - 1

    def __str__(self):
        return "%s %s %s" % (self.team, chr(self.x + ord('a')), (self.y + 1))


    def parseMove(self, move):
        """
        move: string

        move is of the format the referee expects: 'team column(x) row(y)'
        """
        items = move.split(' ') #split by spaces
        self.team = items[0]
        self.x = ord(items[1].lower()) - ord('a')
        self.y = int(items[2])

        return self