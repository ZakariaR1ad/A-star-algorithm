import math
import numpy as np

def get_min(opened):
    min = 0
    for i in range(1, len(opened)):
        if opened[i].f < opened[min].f:
            min = i
    return min

def IsPointInArray(pt,grid):
  for p in grid :
    if(p.x == pt.x and p.y == pt.y): return True
  return False
class Node:
    def __init__(self,x,y,parent,grid = None) -> None:
        self.x = x
        self.y = y
        self.grid = grid
        self.parent = parent
        if parent == None:
            self.g = 0
        else:
            self.g = parent.g + self.distance(parent)
        self.h = 0
        self.f = self.g+self.h
    def distance(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2) #eucludian distance
    def set_h(self,h):
        self.h = h
        self.f = self.g+self.h
    def generate_neighboors(self):
        neighboors = []
        for i in range(-1,2):
            for j in range(-1,2):
              try:
                if i==0 and j==0:
                    continue
                elif(self.grid[self.x+i][self.y+j] == -1):
                    continue
                neighboors.append(Node(self.x+i,self.y+j,self,self.grid))
              except:
                pass
        return neighboors

class A_Star:
    def __init__(self,grid) -> None:
        self.start = None
        self.end = None
        self.grid = grid
    
    def set_start(self,start):
        self.start = start
    
    def set_end(self,end):
        self.end = end
    def retrace_path(self,current):
        path = []
        while current.parent != None:
            path.append(current)
            current = current.parent
        return path
    def find_path(self):
        opened = []
        closed = []
        opened.append(self.start)
        while len(opened) > 0:
            current_index = get_min(opened)
            current = opened.pop(current_index)
            if current.x == self.end.x and current.y == self.end.y:
                return self.retrace_path(current) 
            neighboors = current.generate_neighboors()
            for neighboor in neighboors:
                neighboor.set_h(neighboor.distance(self.end))
                if neighboor.x == self.end.x and neighboor.y == self.end.y:
                    return self.retrace_path(neighboor)
                if IsPointInArray(neighboor,closed):
                    continue
                if IsPointInArray(neighboor,opened):
                    continue
                opened.append(neighboor)
            closed.append(current)
            
        return None
    