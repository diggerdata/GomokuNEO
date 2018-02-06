import copy
import sys

class Board:
    """
     A class the stores the curren game state and has evelution functions to tell
     whose winning and when game is over .
    """
    
    def __init__(self,w=15,h=15,l=5):
        self.cells=[]
        self.goals=[]
        self.activegoals=[]#place to store goals that are active
        self.count=0
        self.length=l
        self.leaf=False
        self.w=w
        self.h=h
        #init other classes
        self.makecells()
    def makecells(self):
        for y in range(self.h):
            xlist=[]
            for x in range(self.w):
                xlist.append(Cell(x,y))
            self.cells.append(xlist)
    def copy(self):
        cells=self.getStates()
        newboard=Board(self.w,self.h,self.length)
        newboard.Load(cells)
        return newboard
                
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
    def getStates(self):
        ans=[]
        ypos=0
        for row in self.cells:
            ans.append([])
            for c in row:
                ans[ypos].append(c.value)
            ypos+=1
        return ans
    def update(self,cell):
        
    def updateGoal(self,start,vel):

    def add(self,c,v):
        ans.append(c[0]+v[0])
        ans.append(c[1]+v[1])
        return ans
    def goalCount(self,start,vel):
        carryon=True
        count=0
        cursor=start.copy()
        v=self.cells[start[1]][start[0]].value
        while carryon:
            cursor = self.add(cursor,vel)
            if v == self.cells[cursor[1]][cursor[0]].value:
                count+=1
            else:
                carryon=False
                

    def getCell(self,x,y):
        #return the value of a cell or null if it outside
        if x<0 or y<0:
            return False
        if x>=self.w or y>=self.h:
            return False
        return self.cells[values]
        


class Cell:
    """
        A class that defines a single cell on the board.
        Initialized to empty cell
    """
    def __init__(self,x,y,v=0):
        self.x=x
        self.y=y
        self.value=v #the values can be 1,0 or -1
        self.played=False
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
