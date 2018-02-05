class Move:
    def __init__(self, team, x, y):
        self.team = team
        self.x = x
        self.y = y

    def __str__(self):
        return "%s %s %s" % (self.team, chr(self.x + ord('a')), (self.y))

    def parseMove(self, move):
        """
        move: string

        move is of the format the referee expects: 'team column(x) row(y)'
        """
        items = move.split(' ') #split by spaces
        team = items[0]
        x = ord(items[1].lower()) - ord('a')
        y = items[2]

        return Move(team, x, y)
