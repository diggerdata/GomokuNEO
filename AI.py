# All the eval functions will be here
from Board import Board
from random import randrange
from math import ceil

testboard = Board(15,15)
class AI:
    def __init__(self,grid=None):
        #initialize the AI
        self.name=0
        self.grid=grid
        self.maxdepth=2
        

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
                if board.isValidMove((x, y)):
                    ans.append((x,y))
        return ans
    def getrandmove(self,board):
        ans=self.getmoves(board)
        return ans[randrange(0,len(ans))]
    def play(self,board):
        return self.getrandmove(board)
    def minmax(self,depth=0):
        #variables
        count=self.grid.count
        moves=self.grid.getmoves()
        scores=[]
        score=None
        for m in moves:
            self.grid.Click(m[0],m[1])
            #getscore
            if self.grid.leaf or depth>=self.maxdepth:
                scores.append(self.grid.getScore())
            else:
                scores.append(self.minmax(depth+1))
            self.grid.clearcell(m[0],m[1])
        if count%2==0:
            score=max(scores)
        else:
            score=min(scores)
        return score

class Grid:
    def __init__(self,board,l):
        self.cells=[]
        self.goals=[]
        self.activegoals=[]#place to store goals that are active
        self.count=0
        self.length=l
        self.leaf=False
        self.w=board.width
        self.h=board.height
        #init other classes
        self.makecells(board)
        self.makegoals()
    def makecells(self,board):
        for y in range(board.height):
            xlist=[]
            for x in range(board.width):
                if board.board[x][y].team is None:
                    xlist.append(Cell(x,y))
                elif board.board[x][y].team is 0:
                    xlist.append(Cell(x,y,1))
                else:
                    xlist.append(Cell(x,y,0))
            self.cells.append(xlist)
    def Load(self,cells):
        self.Clear()
        ypos=0
        for row in cells:
            xpos=0
            for c in row:
                if c!=0:
                    self.cells[ypos][xpos].setvalue(c)
                    self.updateGoals(self.cells[ypos][xpos])
                    self.count+=1
                xpos+=1
            ypos+=1
                    
                    
    def getgoal(self,start,vel,dis):
        ans=[]
        pos=start
        for i in range(dis):
            ans.append(self.cells[pos[1]][pos[0]])
            #move position
            pos[0]+=vel[0]
            pos[1]+=vel[1]
        return ans
    def makegoals(self):
        #vertical
        self.makegset([0,0],[0,1],self.w,(self.h-self.length+1))
        #horizontal
        self.makegset([0,0],[1,0],(self.w-self.length+1),(self.h))
        #positive diagonal
        self.makegset([0,0],[1,1],(self.w-self.length+1),(self.h-self.length+1))
        #negative diagonal
        self.makegset([self.w-1,0],[-1,1],-(self.w-self.length+1)
                      ,(self.h-self.length+1))
        
    def Abs(self,v):
        if v<0:
            return (v*-1)
        return v
    def makegset(self,start,vel,width,height):
        for y in range(0,self.Abs(height)):
            for x in range(0,self.Abs(width)):
                X=x
                Y=y
                if width<0:
                    X*=-1
                if height<0:
                    Y*=-1
                cur=[start[0]+X,start[1]+Y]
                g=Goal(self.getgoal(cur,vel,self.length))
                self.goals.append(g)
    def updateGoals(self,cell):
        self.leaf=False
        for g in cell.Goals:
            if g.active and g not in self.activegoals:
                self.activegoals.append(g)
            elif not g.active and g in self.activegoals:
                self.activegoals.remove(g)
            if g.leaf:
                self.leaf=True
        if len(self.activegoals)==0:
            self.leaf=True
    def Click(self,x,y):
        #determine the value to enter
        v=1
        cell=self.cells[y][x]
        if self.count%2==1:
            v=-1
        if cell.value==0:
            cell.Click(v)
            self.count+=1
            #add new goals to active goals
            self.updateGoals(cell)
    def clearcell(self,x,y):
        cell=self.cells[y][x]
        if cell.value !=0:
            cell.Clear()
            self.count-=1
            self.updateGoals(cell)
    def Clear(self):
        self.goals=[]
        self.activegoals=[]#place to store goals that are active
        self.count=0
        for row in self.cells:
            for c in row:
                c.Clear()
                self.updateGoals(c)
    def getmoves(self):
        ans=[]
        for row in self.cells:
            for c in row:
                if c.value==0:
                    ans.append([c.x,c.y])
        return ans
    def getScore(self):
        total=0
        for a in self.activegoals:
            ans=a.getscore()
            if a.leaf:
                return ans
            total+=ans
        return total
            
        
    def Print(self):
        for y in self.cells:
            for x in y:
                x.Print()
    def PrintGoals(self):
        count=0
        for g in self.goals:
            print(g.getcells())
            count+=1
        print("number of goals are ",count)
    def printgrid(self):
        ans=[]
        for row in self.cells:
            r=[]
            for c in row:
                r.append(c.value)
            ans.append(r)
        print(ans)
class Cell:
    def __init__(self,x,y,v=0):
        self.x=x
        self.y=y
        self.value=v #the values can be 1,0 or -1
        self.Goals=[]# list of goals connected to
    def Click(self,v):
        if self.value==0:
            self.value=v
            self.checkAll()
        else:
            print("There is a problem")
    def setvalue(self,v):
        self.value=v
        self.checkAll()
    def Clear(self):
        #clear the value of a cell and update goals
        self.value=0
        self.checkAll()
        
    def Print(self):
        print([self.x,self.y])
    def checkAll(self):
        #update all goals
        for g in self.Goals:
            g.check()
        
class Goal:
    def __init__(self,cells):
        self.cells=cells
        self.maxscore=100
        self.l=len(cells)
        self.score=0
        self.active= True #if false, goal can never be achieved
        self.leaf=False #is goal achived
        self.addtocells()
        
    def Print(self):
        ans=[]
        for i in range(len(self.cells)):
            ans.append([self.cells[i].x,self.cells[i].y])
        print(ans)
    def addtocells(self):
        for c in self.cells:
            c.Goals.append(self)
        self.check()
    def check(self):
        seenx=0
        seeno=0
        count=0
        self.leaf=False
        for c in self.cells:
            if c.value==1:
                seenx=1
            if c.value==-1:
                seeno=1
            if c.value is not 0:
                count+=1
        if (seenx==1 and seeno==1):
            #print("caught you")
            self.active=False
            self.score=0
        elif seeno==0 and seenx==0:
            self.active=False
        else:
            self.active=True
            self.score=count/self.l
            if seeno==1:
                self.score*=-1
        if count == self.l and self.active:
            self.leaf = True
    def getcells(self):
        ans=[]
        for c in self.cells:
            ans.append([c.x,c.y])
        return ans
    def getscore(self):
        ans=0
        if self.score<1:
            ans=self.score/15
        if self.leaf:
            if self.score>0:
                return self.maxscore
            return -self.maxscore
        ans*=self.maxscore
        return ans
                
def printgoal(g):
    for i in g:
        cells=i.getcells()
        print(cells)
def main():
    testb=Board(3,3)
    testAI=AI();
    print(testAI.play(testboard));
    #grid = Grid(testboard,5)
    #grid.Print()
    #printgoal(grid.getgoal([1,1],[1,1],5))
    grid1=Grid(testb,3)
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
    grid1.Load([[1,0,0],[0,-1,0],[0,-1,1]])
    player=AI(grid1)
    print("The score is ",player.minmax())
   
    
# main()
    
