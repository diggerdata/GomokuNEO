from Board import Board
from AI import AI
from Move import Move
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os

# The player object to be created in the watchdog callback
ai = AI()
move_file = './move_file'
myTurn = False


class Player:
    class TurnFileHandler(PatternMatchingEventHandler):
        """
        Event handler to watch current directory for when the team's 
        file is created
        """

        # patterns = ['.\gomokuneo.go', '.\goneo.go']

        def __init__(self, team_name):
            super().__init__()
            self._patterns = ['./{0}.go'.format(team_name)]

        def process(self, event):
            global myTurn
            print(event.src_path, event.event_type)
            myTurn = True

        def on_created(self, event):
            self.process(event)

        def on_modified(self, event):
            self.process(event)

    def __init__(self, engine, name, timeout=10):
        """
        name: string
        timeout: int (default 10) 

        name is the name of the player (individual/team)
        timeout is the time limit for a move, in seconds
        """
        self.timeout = timeout
        self.name = name
        game = engine

        # start watching
        self.observer = Observer()
        self.observer.schedule(self.TurnFileHandler(name), '.', recursive=True)
        self.observer.start()
        try:
            while True:
                if myTurn == True:
                    readMoveFile(game.getBoard())
                    coords = ai.play(game.getBoard(), t=9.0)
                    move = Move(name, coords[0], coords[1])
                    game.getBoard().Click(coords[0], coords[1])
                    writeMoveFile(name, move)
                    time.sleep(1)
                else:
                    print('Waiting turn...')

        except Exception as err:
            self.observer.stop()
            print('Error: {0}'.format(err))

        self.observer.join()


def readMoveFile(board):
    with open(move_file) as fp:
        line = fp.readline()
        if line:
            move = Move()
            move.parseMove(line)
            board.Click(move.x, move.y)


def writeMoveFile(team, move):
    with open(move_file, 'w') as fp:
        fp.write(move.__str__())
        global myTurn
        myTurn = False
