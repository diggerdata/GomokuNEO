# All the eval functions will be here
from Board import Board
from random import randrange

testboard = Board(15,15)
class AI:
    def __init__(self):
        #initialize the AI
        self.name=0
        

    def play(self,board):
        #get possible moves and play them
        return 0
    def Eval(self,board):
        #return a current score for the board
        return 0
    def getmoves(self,board):
        ans=[]
        for y in range(board.height):
            for x in range(board.width):
                if board.board[x][y].team is None:
                    ans.append((x,y))
        return ans
    def getrandmove(self,board):
        ans=self.getmoves(board)
        return ans[randrange(0,len(ans))]
    def play(self,board):
        return self.getrandmove(board)
        


def main():
    testAI=AI()
    print(testAI.play(testboard))
# main()
    
