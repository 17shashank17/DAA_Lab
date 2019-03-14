from collections import defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def printt(self):
        print(self.graph)

    def bfs(self,u):
        visited=[False]*len(self.graph)
        queue=[]
        visited[u]=True
        queue.append(u)
        while queue:
            x=queue.pop()
            print(x,end=" ")
            for i in self.graph[x]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

g=graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(2,3)
g.printt()
g.bfs(0)