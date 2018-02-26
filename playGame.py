#play two Ai's against each other
from Board import Board
from AI import AI
from AI2 import AI2
import timeit
#class
class player:
    def __init__(self,name,ai,board,t=1):
        self.brain=ai
        self.board=board
        self.name=name
        self.time=t
        self.wins=0
        self.losses=0
        self.draws=0
    def reset(self):
        self.wins=0
        self.losses=0
        self.draws=0
    def play(self,board):
        self.board.load(board.getStates())
        return self.brain.play(self.board,self.time)

def playgame(first,second):
    gboard=Board(15,15,5)
    while not gboard.leaf:
        m=None
        if gboard.count%2==0:
            m=first.play(gboard)
        else:
            m=second.play(gboard)
        gboard.Click(m[0],m[1])
        print("new state")
        gboard.printBoard()
        print(first.name,"'s score is ",first.brain.score)
        print(second.name,"'s score is ",second.brain.score)
    score=gboard.getScore()
    if score>85:
        first.wins+=1
        second.losses+=1
        print(first.name," wins")
    elif score<-85:
        first.losses+=1
        second.wins+=1
        print(second.name," wins")
    else:
        first.draws+=1
        second.draws+=1
        print("It is a draw")
        
def playfair(p1,p2):
    playgame(p1,p2)
    playgame(p2,p1)


        
    
def gameloop(player1,player2,board):
    print("start ",timeit.default_timer())  
    while not board.leaf:
        m=None
        if board.count%2==0:
            m=player1.play(board,9)
        else:
            m=player2.play(board,9)
        board.Click(m[0],m[1])
        print("new state")
        board.printBoard()
        print("player 1's score is ",player1.score)
        print("player 2's score is ",player2.score)
        print("time taken ",timeit.default_timer()) 
    score=board.getScore()
    if score>85:
        print("player1 wins")
    elif score<-85:
        print("player2 wins")
    else:
        print("It is a draw")
    

def main():
    board= Board(5,5,4)
    player1=AI()
    player2=AI()
    player1.maxdepth=2
    player2.maxdepth=2
    gameloop(player1,player2,board)
    
def league(no):
    brain1=AI()
    brain2=AI2()
    b=Board(15,15,5)
    p1=player("Normal",brain1,b.copy(),7)
    p2=player("quiter",brain2,b.copy(),7)
    print("league is starting")
    for i in range(no):
        playfair(p1,p2)
    if p1.wins>p2.wins:
        print(p1.name," wins with ",p1.wins," wins ",p1.losses," losses and ",p1.draws," draws")
    elif p2.wins>p1.wins:
        print(p2.name," wins with ",p2.wins," wins ",p2.losses," losses and ",p2.draws," draws")
    else:
        print("they drew")
    
league(7)
