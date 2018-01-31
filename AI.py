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
    def __init__(self,board):
        self.cells=[]
        self.goals=[]
        self.makecells(board)
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
        no=1
    def Print(self):
        for y in self.cells:
            for x in y:
                x.Print()
            
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
    def Print(self):
        print([self.x,self.y])
        
class Goals:
    def __init__(self,cells):
        self.cells=cells
        self.score=0
        self.active= True #it false, it means that the goal can never be achieved
    def Print(self):
        ans=[]
        for i in range(len(self.cells)):
            ans.append([self.cells[i].x,self.cells[i].y])
        print(ans)
def printgoal(g):
    for i in g:
        i.Print()
def main():
    testAI=AI();
    print(testAI.play(testboard));
    grid = Grid(testboard)
    #grid.Print()
    printgoal(grid.getgoal([1,1],[1,1],5))
    
main()
    
