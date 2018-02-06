import copy
import sys
from random import randrange

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
        self.makegoals()
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
    def getbestmoves(self):
        if self.count==0:
            return self.getmoves()
        moves=[]
        for g in self.activegoals:
            for c in g.cells:
                m=[c.x,c.y]
                if c.value==0 and (m not in moves):
                    moves.append(m)
        return moves
    def getquickmoves(self):
        if self.count==0:
            return self.getmoves()
        bcount=0
        #get best count
        for g in self.activegoals:
            if bcount<g.count:
                bcount=g.count
        moves=[]
        for g1 in self.activegoals:
            if g1.count==bcount:
                for c in g1.cells:
                    m=[c.x,c.y]
                    if c.value==0 and (m not in moves):
                        moves.append(m)
        return moves
    def getfastmoves(self):
        if self.count==0:
            return self.getmoves()
        moves=[]
        for g in self.activegoals:
            for c in g.cells:
                m=[c.x,c.y]
                if c.value==0 and (m not in moves):
                    moves.append(m)
        return moves
    def getnicemoves(self):
        goals=[]
        bcount=0
        for g in self.activegoals:
            if bcount<g.count:
                bcount=g.count
                goals=[]
                goals.append(g)
            elif bcount==g.count:
                goals.append(g)
        moves=[]
        scores=[]
        for g in goals:
            m=g.getbestmove()
            if (m!= None) and (m not in moves):
                moves.append(m)
                scores.append(self.cells[m[1]][m[0]].count)
        if len(moves)==0:
            print("Huge problem")
            return self.getquickmoves()
        moves=self.sort(moves,scores)
        if self.count%2==1:
            moves.reverse()
        return moves
                
                
    def getScore(self,depth=0):
        total=0
        for a in self.activegoals:
            ans=a.getscore()
            if a.leaf:
                if self.count%2==0:
                    ans+=(depth*1)
                else:
                    ans-=(depth*1)
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
    def printBoard(self):
        output = ''
        output += '{0} -- {1}\n'.format('X', teams[0])
        output += '{0} -- {1}'.format('O', teams[1])
        output += '\n   '
        for x in range(self.width):
            output += '{0} '.format(chr(x+ord('A')))
        output += "\n"
        for y in range(self.height):
            output += '{0:2d} '.format(y+1)
            for x in range(self.width):
                if self.board[x][y].team is None:
                    output += '-'
                else:
                    if teams.index(self._field[x][y].team) == 0:
                        team_color = 'X'
                    else:
                        team_color = 'O'
                    output += team_color
                output += ' '
            output += '\n'
        print(output)
    def printBoard(self):
        for row in self.cells:
            output=""
            for c in row:
                if c.value==1:
                    output+="X"
                elif c.value==-1:
                    output+="O"
                else:
                    output+="_"
            print(output)
        


class Cell:
    """
        A class that defines a single cell on the board.
        Initialized to empty cell
    """
    def __init__(self,x,y,v=0):
        self.x=x
        self.y=y
        self.value=v #the values can be 1,0 or -1
        self.count=0 #no of activegoals connected to
        self.Goals=[]# list of goals connected to
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
        self.count=0
        #update all goals
        for g in self.Goals:
            g.check()
            if g.active:
                self.count+=g.score
        
class Goal:
    """
        A class consisiting of a group of cells that must be activated to
        achieve a goal
    """
    def __init__(self,cells):
        self.cells=cells
        self.maxscore=100
        self.l=len(cells)
        self.score=0
        self.count=0
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
            self.count=0
        elif seeno==0 and seenx==0:
            self.active=False
        else:
            self.active=True
            self.score=count/self.l
            self.count=count
            if seeno==1:
                self.score*=-1
        if count == self.l and self.active:
            self.leaf = True
    def getcells(self):
        ans=[]
        for c in self.cells:
            ans.append([c.x,c.y])
        return ans
    def getbestmove(self):
        count=0
        ms=[]
        for c in self.cells:
            if c.count>count and c.value==0:
                count=c.count
                ms=[]
                ms.append([c.x,c.y])
            elif c.count==count and c.value==0:
                ms.append([c.x,c.y])
        if len(ms)>0:
            return ms[randrange(0,len(ms))]
        return None
        
                
    def getscore(self):
        ans=0
        if self.score<1:
            #ans=self.score/15
            ans=(self.score**2)/30
        if self.leaf:
            if self.score>0:
                return self.maxscore
            return -self.maxscore
        ans*=self.maxscore
        return ans
