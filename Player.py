# import Board as b
import AI as ai
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

# The player object to be created in the watchdog callback
player = None

class Player:
    def __init__(self, board_size=15, player=0, timeout=10):
        """
        board_size: int (default 15)
        player: int (default 0)
        timeout: int (default 10)

        board_size is the size of the board (board_size x board_size)
        player is the player number (0 = first, 1 =  second)
        timeout is the timeout limit
        """
        self.board_size = board_size
        self.player = player
        self.time_limit = time_limit

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
        if event.is_directory:
            return None

        elif event.event_type == 'created' and event.src_path == "./GomokuNEO.go":
            global player
            file_name = './move_file'
            try:
                if os.stat(file_name).st_size == 0 and player is None:
                    # Do this if we are the first player
                    print("We are the first player! \nCreating player...")
                    player = Player(player=0)
                    
                elif player is not None:
                    # Do play game stuff here

                else:
                    # Do this if we are the second player
                    print("We are the second player! \nCreating player...")
                    player = Player(player=1)
            except IOError:
                print("Could not read %s." % file_name)
            # Take any action here when a file is first created.

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print("Received modified event - %s." % event.src_path)

if __name__ == "__main__":
    w = Watcher()
    w.run()