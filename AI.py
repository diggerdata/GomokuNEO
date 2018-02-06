# All the eval functions will be here
from Board import Board
from random import randrange
from math import ceil


class AI:
    def __init__(self,b=None):
        #initialize the AI
        self.name=0
        self.time=0
        self.score=0
        self.depths=[]#testing
        if b!=None:
            self.board=b.copy()
        self.maxdepth=5
        for i in range(self.maxdepth):
            self.depths.append([])
    def getrandmove(self,board=None):
        if board!= None:
            self.board=board.copy()
        ans=self.board.getmoves()
        return ans[randrange(0,len(ans))]
    def sort(self,moves,scores):
        newmoves=[]
        saves=[]
        while len(newmoves)<len(moves):
            b=self.getmax(scores,saves)
            no=0
            for s in scores:
                if s==b:
                    newmoves.append(moves[no])
                no+=1
            saves.append(b)
        return newmoves
                    
    def getmax(self,scores,saves):
        ans=min(scores)
        for s in scores:
            if ans<s and (s not in saves):
                ans=s
        return ans
        
    def quickmove(self,board=None):
        if board!= None:
            self.board=board.copy()
        moves=self.board.getmoves()
        scores = self.alphabeta()
        score=0
        if self.board.count%2==0:
            score=max(scores)
        else:
            score=min(scores)
        pans=[]
        no=0
        self.score=score
        for s in scores:
            if score==s:
                pans.append(moves[no])
            no+=1
        #return random best move
        print("possible moves are ",pans)
        return pans[randrange(0,len(pans))]
    def getmove(self,board=None):
        if board!= None:
            self.board=board.copy()
        moves=self.board.getmoves()
        scores = self.getabmove()
        score=0
        if self.board.count%2==0:
            score=max(scores)
        else:
            score=min(scores)
        pans=[]
        no=0
        self.score=score
        for s in scores:
            if score == s:
                pans.append(moves[no])
            no+=1
        #return random best move
        print("possible moves are ",pans)
        return pans[randrange(0,len(pans))]
        
    def play(self,board):
        #return self.getrandmove(board)
        self.board=board.copy()
        return self.getABmove(board)
    def getabmove(self,board=None):
        if board!=None:
            self.board=board.copy()
        moves=self.board.getmoves()
        scores=[]
        for m in moves:
            self.board.Click(m[0],m[1])
            scores.append(self.alphabeta(-10000,10000,1))
            self.board.clearcell(m[0],m[1])
        score=0
        if self.board.count%2==0:
            score=max(scores)
        else:
            score=min(scores)
        self.score=score
        pans=[]
        no=0
        for s in scores:
            if score==s:
                pans.append(moves[no])
            no+=1
        #return random best move
        print("possible moves are ",pans)
        return pans[randrange(0,len(pans))]
    def getABmove(self,board=None):
        if board!=None:
            self.board=board.copy()
        if self.board.count==0:
            return self.getrandmove()
        moves=self.board.getnicemoves()
        scores=[]
        for m in moves:
            self.board.Click(m[0],m[1])
            scores.append(self.AlphaBeta(-10000,10000,1))
            self.board.clearcell(m[0],m[1])
        score=0
        if self.board.count%2==0:
            score=max(scores)
        else:
            score=min(scores)
        self.score=score
        pans=[]
        no=0
        for s in scores:
            if score==s:
                pans.append(moves[no])
            no+=1
        #return random best move
        print("possible moves are ",pans)
        return pans[randrange(0,len(pans))]
    def getdeepmove(self,t,moves,depth):
        scores=[]
        for m in moves:
            self.board.Click(m[0],m[1])
            scores.append(self.AlphaBeta(-10000,10000,1))
            self.board.clearcell(m[0],m[1])
        #sort
        moves=self.sort(moves,scores)
        if self.board.count%2==1:
            moves.reverse()
        return moves
    def deepingmove(self,board,t=1):
        if self.board.count==0:
            return self.getrandmove()#modify
        depth=1
        moves=self.board.getbestmoves()
        
    def minmax(self,depth=0):
        if depth==0:
            self.time=0
        #variables
        count=self.board.count
        moves=self.board.getmoves()
        scores=[]
        score=None
        mno=0
        index=0
        for m in moves:
            self.board.Click(m[0],m[1])
            ans=None
            #getscore
            if self.board.leaf or depth>=self.maxdepth:
                ans=self.board.getScore()
            else:
                ans=self.minmax(depth+1)
            #ans-=(depth*ans*0.0001)
            scores.append(ans)
            self.depths.append(self.board.getStates())
            self.board.clearcell(m[0],m[1])
            #print("depth is ",depth+1," score is ",ans,"index is ",index)
            index+=1
        self.time+=1
        #if depth is 0 return list of scores
        no=0
        if depth==0:
            return scores
        if count%2==0:
            score=max(scores)
        else:
            score=min(scores)
        return score
    def MinMax(self,depth=0):
        if depth==0:
            self.time=0
        moves=self.board.getbestmoves()
        #variables
        count=self.board.count
        scores=[]
        score=None
        index=0
        for m in moves:
            self.board.Click(m[0],m[1])
            ans=None
            #getscore
            if self.board.leaf or depth>=self.maxdepth:
                ans=self.board.getScore()
            else:
                ans=self.MinMax(depth+1)
            ans-=(depth*0.001)
            depth+=1
            scores.append(ans)
            self.board.clearcell(m[0],m[1])
        self.time+=1
        #if depth is 0 return list of scores
        if depth==0:
            return scores
        if count % 2 == 0:
            score = max(scores)
        else:
            score = min(scores)
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
        index=0
        for m in moves:
            if alpha <= beta:
                self.board.Click(m[0], m[1])
                ans = None
                # getscore
                if self.board.leaf or depth >= self.maxdepth:
                    ans = self.board.getScore()
                else:
                    ans = self.alphabeta(alpha, beta, depth + 1)
                scores.append(ans)
                if count%2==0:
                    if score<ans:
                        score=ans
                    if alpha<ans:
                        alpha=ans
                else:
                    if score>ans:
                        score=ans
                    if beta>ans:
                        beta=ans
                #self.board.printBoard()
                self.board.clearcell(m[0],m[1])#undo last move
                #print("normal move ",m)
            #prune
            else:
                if repeat:
                    n=o
                    print("What!")
                repeat=True
                break
            index+=1
        self.time+=1
        return score
    def AlphaBeta(self,alpha=-10000,beta=10000,depth=0):
        if depth==0:
            self.time=0
        #variables
        count=self.board.count
        moves=self.board.getnicemoves()
        scores=[]
        score=-10000
        if count%2==1:
            score=10000
        repeat = False
        index=0
        for m in moves:
            if alpha<=beta:
                self.board.Click(m[0],m[1])
                ans=None
                #getscore
                if self.board.leaf or depth>=self.maxdepth:
                    ans=self.board.getScore(depth)
                else:
                    ans = self.alphabeta(alpha,beta,depth+1)
                mult=1
                if ans<0:
                    mult=-1
                scores.append(ans)
                if count%2==0:
                    if score<ans:
                        score=ans
                    if alpha<ans:
                        alpha=ans
                else:
                    if score>ans:
                        score=ans
                    if beta>ans:
                        beta=ans
                #self.board.printBoard()
                self.board.clearcell(m[0],m[1])#undo last move
                #print("normal move ",m)
            #prune
            else:
                if repeat:
                    n=o
                    print("What!")
                repeat=True
                break
            index+=1
        self.time+=1
        return score
    def printBoard(self):
        output=""
        dno=0
        for d in self.depths:
            for r in d:
                for c in r:
                    if c==1:
                        output+="X"
                    elif c==-1:
                        output+="O"
                    else:
                        output+="_"
                output+="\n"
                
        print(output)


def printgoal(g):
    for i in g:
        cells = i.getcells()
        print(cells)


def main():
    n=0
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
    grid1.Click(2, 2)
    grid1.Click(0, 0)
    grid1.Click(1, 1)
    grid1.Click(1, 0)
    grid1.Click(1, 2)
    grid1.Click(2, 0)
    printgoal(grid1.activegoals)
    grid1.printgrid()
    print("score is ", grid1.getScore())
    print("loading")
    grid1.load([[1, 0, 0], [], [-1, 0]])
    printgoal(grid1.activegoals)
    grid1.printgrid()
    print("score is ", grid1.getScore())
    print("moves are ", grid1.getmoves())
    print("Min Max test ")
    grid1.Load([[0,0,0],
                [0,1,0],
                [0,0,0]])
    player=AI(grid1)
    print("player count is ",player.board.count)
    print("Minmax scores are ",player.minmax())
    print("player count is ",player.board.count)
    print("AlphaBeta scores are ",player.getABmove())
    grid1.printBoard()
    #print("Move is ",player.getmove())
    print("testing sort")
    l=[5,7,1,4,3,2,8,9,0,1]
    print("Before ",l)
    nl=player.sort(l,l.copy())
    print("After ",nl)
    
    
main()
    
