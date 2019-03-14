from collections import defaultdict
class graph:
    def __init__(self,n):
        self.graph=defaultdict(list)
        self.distances={}
        self.color=['white']*n
        self.size=n
        self.dist=[100000]*n
        self.visited={}
        self.dist[0]=0
    
    def addedge(self,u,v,d):
        self.graph[u].append(v)
        self.distances[u,v]=d
        self.visited[u,v]=False
        
    def printt(self):
        print(self.graph)
        print(self.distances)

    def print_dist(self):
        print(self.dist)

    def dijkstra(self,s):
        self.color[s]='grey'
        for i in self.graph[s]:
            if self.visited[s,i] is False:
                if self.dist[i]>self.dist[s]+self.distances[s,i]:
                    self.dist[i]=self.dist[s]+self.distances[s,i]
                self.visited[s,i]=True
                self.dijkstra(i)
        

g=graph(5)
g.addedge(0,1,10)
g.addedge(1,2,1)
g.addedge(2,3,6)
g.addedge(3,2,4)
g.addedge(4,3,2)
g.addedge(4,2,9)
g.addedge(0,4,5)
g.addedge(4,1,3)
g.addedge(1,4,2)
#g.printt()
g.dijkstra(0)
g.print_dist()

