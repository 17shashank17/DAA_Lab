from collections import defaultdict
class graph:
    def __init__(self,n):
        self.matrices=[[0 for i in range(n)] for j in range(n)]
        self.vertices=n
        self.distances=[[-1 for i in range(n)] for j in range(n)]

    def addedge(self,u,v,d):
        self.matrices[u][v]=1
        self.distances[u][v]=d

    def floyd_warshell(self):
        for i in range(self.vertices):
            self.distances[i][i]=0

        for i in range(0,self.vertices):
            for j in range(self.vertices):
                if self.matrices[i][j]==0:
                    self.distances[i][j]=float("inf")

        for i in range(self.vertices):
            self.distances[i][i]=0

        self.prinnt()

        for k in range(0,self.vertices):
            for i in range(0,self.vertices):
                for j in range(0,self.vertices):
                    self.distances[i][j]=min(self.distances[i][j],self.distances[i][k]+self.distances[k][j])

    def prinnt(self):
        for i in range(0,self.vertices):
            for j in range(self.vertices):
                print(self.distances[i][j],end=" ")
            print()

g=graph(3)
g.addedge(0,1,2)
g.addedge(0,2,3)
g.addedge(2,1,3)
g.addedge(1,2,1)
g.floyd_warshell()
g.prinnt()
        
