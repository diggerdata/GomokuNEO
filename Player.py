from Board import Board
from AI import AI
from Move import Move
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler
import os

# The player object to be created in the watchdog callback
ai = AI()
move_file = '.\move_file'
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
            self._patterns = ['.\{0}.go'.format(team_name)]

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
        global game
        game = engine

        #start watching
        self.observer = Observer()
        self.observer.schedule(self.TurnFileHandler(name), '.', recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
                if myTurn == True:
                    (x, y) = ai.play(game.getBoard())
                    writeMoveFile(name, x, y)
                else:
                    print('Waiting turn...')
        except Exception as err:
            self.observer.stop()
            print('Error: {0}'.format(err))

        self.observer.join()



def readMoveFile():
    with open(move_file) as fp:
        my_move = Move()
        return Move.parse_move(my_move, fp.readline())

def writeMoveFile(team, x, y):
    move = Move(team, x, y)
    with open(move_file, 'w') as fp:
        fp.write(move.__str__())
        global myTurn
        myTurn = False



class Watcher:
    # Make sure to run script in the same directory as the ref
    DIRECTORY_TO_WATCH = "./"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

class Handler(FileSystemEventHandler):
    
    @staticmethod
    def on_any_event(event):
        global player
        global board
        global move_file
        player_file = '.\{0}.go'.format(player.name)
        
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            if event.src_path == player_file:
                try:
                    if os.stat(file_name).st_size == 0 and player is None and board is None:
                        # Do this if we are the first player
                        print("We are the first player! \nCreating player...")
                        board = Board()
                        player = Player(board, player=0)
                        print(board)
                    elif player is not None and board is not None:
                        # Do what we do when it is our turn
                        print('Getting move...')
                        print(player.AI.play(board))
                    else:
                        print("We are the second player! \nCreating player...")
                        player = Player(board, player=1)
                except:
                    print("Could not read %s." % file_name)
            elif event.src_path.endswith('.go'):
                if board is None:
                    board = Board()
                    print(board)
                else:
                    # Add other player's move to board
                    pass

            # Take any action here when a file is first created.

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print("Received modified event - %s." % event.src_path)




# if __name__ == "__main__":
#     w = Watcher()
#     w.run()