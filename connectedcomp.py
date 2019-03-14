from collections import defaultdict
class graph:
    def __init__(self,n):
        self.graphs=defaultdict(list)
        self.size=n

    def add(self,u,v):
        self.graphs[u].append(v)
        self.graphs[v].append(u)

    def adj_list_print(self):
        print(self.graphs)

    def bfs(self,u):
        visited=[False]*self.size
        queue=[]
        l=[]
        visited[u]=True
        queue.append(u)
        while queue:
            print(queue.pop(0),end=" ")
            for i in self.graphs[u]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
    
    def con_comp(self):
        count=0
        visited=[False]*self.size
        for i in range(self.size):
            if visited[i]==False:
                count+=1
                self.bfs(i)
                visited[i]=True
                print()
        print("Com: ",count)


        

g=graph(6)
g.add(0,1)
g.add(0,2)
g.add(2,3)
g.add(4,5)
g.adj_list_print()
g.con_comp()

