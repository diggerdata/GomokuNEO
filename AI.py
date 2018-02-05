# All the eval functions will be here
from Board import Board
from random import randrange
from math import ceil

testboard = Board(15,15,5)
class AI:
    def __init__(self,b=None):
        #initialize the AI
        self.name=0
        self.time=0
        if b!=None:
            self.board=b.copy()
        self.maxdepth=5
    def getrandmove(self,board):
        ans=self.getmoves(board)
        return ans[randrange(0,len(ans))]
    def getmove(self,board=None):
        if board!= None:
            self.board=board.copy()
        moves=self.board.getmoves()
        scores = self.minmax()
        score=0
        if self.board.count%2==0:
            score=max(scores)
        else:
            score=min(scores)
        pans=[]
        no=0
        for s in scores:
            if score==s:
                pans.append(moves[no])
            no+=1
        #return random best move
        return pans[randrange(0,len(pans))]
        
    def play(self,board):
        #return self.getrandmove(board)
        self.board=board.copy()
        return self.getmove(board)
    def minmax(self,depth=0):
        if depth==0:
            self.time=0
        #variables
        count=self.board.count
        moves=self.board.getmoves()
        scores=[]
        score=None
        for m in moves:
            self.board.Click(m[0],m[1])
            #getscore
            if self.board.leaf or depth>=self.maxdepth:
                scores.append(self.board.getScore())
            else:
                scores.append(self.minmax(depth+1))
            self.board.clearcell(m[0],m[1])
        self.time+=1
        #if depth is 0 return list of scores
        if depth==0:
            return scores
        if count%2==0:
            score=max(scores)
        else:
            score=min(scores)
        return score
    def alphabeta(self,alpha=-10000,beta=10000,depth=0):
        if depth==0:
            self.time=0
        #variables
        count=self.board.count
        moves=self.board.getmoves()
        scores=[]
        score=-10000
        if count%2==1:
            score=10000
        repeat = False
        for m in moves:
            if alpha<beta:
                self.board.Click(m[0],m[1])
                ans=None
                #getscore
                if self.board.leaf or depth>=self.maxdepth:
                    ans=self.board.getScore()
                else:
                    ans = self.alphabeta(alpha,beta,depth+1)
                scores.append(ans)
                if count%2==0:
                    if score<ans:
                        score=ans
                        alpha=ans
                else:
                    if score>ans:
                        score=ans
                        beta=ans
                self.board.clearcell(m[0],m[1])#undo last move
                #print("normal move ",m)
            #prune
            else:
                if repeat:
                    print("What!")
                repeat=True
                break
        self.time+=1
        #if depth is 0 return list of scores
        if depth==0:
            return scores
        return score



                
def printgoal(g):
    for i in g:
        cells=i.getcells()
        print(cells)
def main():
    testb=Board(3,3,3)
    testAI=AI();
    #print(testAI.play(testboard));
    #grid = Grid(testboard,5)
    #grid.Print()
    #printgoal(grid.getgoal([1,1],[1,1],5))
    grid1=Board(3,3,3)
    #grid.PrintGoals()
    print("The grid layout is ")
    grid1.printgrid()
    print("testing")
    grid1.Click(2,2)
    grid1.Click(0,0)
    grid1.Click(1,1)
    grid1.Click(1,0)
    grid1.Click(1,2)
    grid1.Click(2,0)
    printgoal(grid1.activegoals)
    grid1.printgrid()
    print("score is ",grid1.getScore())
    print("loading")
    grid1.Load([[1,0,0],[],[-1,0]])
    printgoal(grid1.activegoals)
    grid1.printgrid()
    print("score is ",grid1.getScore())
    print("moves are ",grid1.getmoves())
    print("Min Max test ")
    grid1.Load([[0,0,0],
                [0,1,0],
                [0,0,0]])
    player=AI(grid1)
    print("Minmax scores are ",player.minmax())
    print("AlphaBeta scores are ",player.alphabeta())
    #print("Move is ",player.getmove())
    
main()
    
