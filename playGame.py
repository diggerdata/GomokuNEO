#play two Ai's against each other
from Board import Board
from AI import AI
import timeit
def gameloop(player1,player2,board):
    print("start ",timeit.default_timer())  
    while not board.leaf:
        m=None
        if board.count%2==0:
            m=player1.play(board,9.0)
        else:
            m=player2.play(board,9.0)
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
    board= Board(15,15,5)
    player1=AI()
    player2=AI()
    player1.maxdepth=2
    player2.maxdepth=2
    gameloop(player1,player2,board)
    
main()
