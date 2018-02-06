#play two Ai's against each other
from Board import Board
from AI import AI
def gameloop(player1,player2,board):
    while not board.leaf:
        m=None
        if board.count%2==0:
            m=player1.play(board)
        else:
            m=player2.play(board)
        board.Click(m[0],m[1])
        print("new state")
        board.printBoard()
        print("player 1's score is ",player1.score)
        print("player 2's score is ",player2.score)
    score=board.getScore()
    if score>95:
        print("player1 wins")
    elif score<-95:
        print("player2 wins")
    else:
        print("It is a draw")

def main():
    board= Board(7,7,4)
    player1=AI()
    player2=AI()
    player1.maxdepth=2
    player2.maxdepth=2
    gameloop(player1,player2,board)
    
main()
