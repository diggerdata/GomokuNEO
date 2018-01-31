from Board import Board
# from AI import AI
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

# The player object to be created in the watchdog callback
player = None
board = None

class Player:
    def __init__(self, board, player=0, timeout=10):
        """
        board: Board Object
        player: int (default 0)
        timeout: int (default 10)

        board is a Board object
        player is the player number (0 = first, 1 =  second)
        timeout is the timeout limit in seconds
        """
        self.board = board
        self.player = player
        self.timeout = timeout

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
        
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            file_name = './move_file'
            if event.src_path == "./GomokuNEO.go":
                try:
                    if os.stat(file_name).st_size == 0 and player is None and board is None:
                        # Do this if we are the first player
                        print("We are the first player! \nCreating player...")
                        board = Board()
                        player = Player(board, player=0)
                        print(board)
                    elif player is not None and board is not None:
                        # Do what we do when it is our turn
                        pass
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

if __name__ == "__main__":
    w = Watcher()
    w.run()