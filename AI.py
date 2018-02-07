# All the eval functions will be here
from Board import Board
from random import randrange
from math import ceil
import timeit


testboard = Board(15,15,5)
class AI:
    def __init__(self,b=None):
        #initialize the AI
        self.name=0
        self.time=0
        self.score=0
        self.timelimit=0 # return if the time limit is pased
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
        scores = self.minmax()
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
        
    def play(self,board,t=9.0):
        #return self.getrandmove(board)
        self.board=board.copy()
        return self.getgoodmove(board,t)
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
    def getmovefrommoves(self,moves,scores):
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
        #print("possible moves are ",pans)
        return pans[randrange(0,len(pans))]
    def getgoodmove(self,board,limit):
        self.board=board.copy()
        self.timelimit= timeit.default_timer()+limit
        currenttime=timeit.default_timer()
        self.maxdepth=1
        moves=self.board.getnicemoves()
        move=self.getrandmove()
        while timeit.default_timer()<self.timelimit:
            scores=[]
            for m in moves:
                self.board.Click(m[0],m[1])
                scores.append(self.AlphaBeta(-10000,10000,1))
                self.board.clearcell(m[0],m[1])
                if timeit.default_timer()>self.timelimit:
                    print("depth reached ",self.maxdepth)
                    return move
            move=self.getmovefrommoves(moves,scores)
            moves=self.sort(moves,scores)
            if self.board.count%2==1:
                moves.reverse()
            self.maxdepth+=1
        print("depth reached wow",self.maxdepth)
        return move
        
        
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
            if alpha<beta and timeit.default_timer()<self.timelimit:
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
    def AlphaBeta(self,alpha=-10000,beta=10000,depth=0,moves=None):
        if depth==0:
            self.time=0
        #variables
        count=self.board.count
        if moves==None:
            moves=self.board.getnicemoves(depth)
        scores=[]
        score=-10000
        if count%2==1:
            score=10000
        repeat = False
        index=0
        for m in moves:
            if alpha<beta and timeit.default_timer()<self.timelimit:
                self.board.Click(m[0],m[1])
                ans=None
                carryon=True
                #getscore
                if self.board.leaf:
                    ans=self.board.getScore(depth)
                elif depth>=self.maxdepth:
                    qm=self.board.getquitemoves()
                    if len(qm)==0:
                        ans=self.board.getScore(depth)
                    else:
                        ans = self.AlphaBeta(alpha,beta,depth+1,qm)
                else:
                    ans = self.AlphaBeta(alpha,beta,depth+1)
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

    
