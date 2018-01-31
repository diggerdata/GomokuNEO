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

class Grid:
    def __init__(self,board,l):
        self.cells=[]
        self.goals=[]
        self.length=l
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
class Cell:
    def __init__(self,x,y,v=0):
        self.x=x
        self.y=y
        self.value=v #the values can be 1,0 or -1
        self.Goals=[]# list of goals connected to
    def click(self,v):
        if self.value==0:
            self.value=v
        else:
            print("There is a problem")
        self.checkAll()
    def setvalue(self,v):
        self.value=v
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
        self.l=len(cells)
        self.score=0
        self.active= True #it false, it means that the goal can never be achieved
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
        x=0
        o=0
        count=0
        for c in self.cells:
            if c.value==1:
                x=1
            if c.value==-1:
                o=1
            if c.value is not 0:
                count+=1
        if x==1 and o==1:
            self.active=False
            self.score=0
        else:
            self.active=True
            self.score=count/self.l
    def getcells(self):
        ans=[]
        for c in self.cells:
            ans.append([c.x,c.y])
        return ans
                
def printgoal(g):
    for i in g:
        i.Print()
def main():
    testb=Board(3,3)
    testAI=AI();
    print(testAI.play(testboard));
    grid = Grid(testboard,5)
    #grid.Print()
    #printgoal(grid.getgoal([1,1],[1,1],5))
    #grid1=Grid(testb,3)
    grid.PrintGoals()
main()
    
