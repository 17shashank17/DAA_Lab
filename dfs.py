from collections import defaultdict
class graph:
    def __init__(self,n):
        self.vertices=n
        self.dict=defaultdict(list)
        self.color=['white']*n
        self.start_time=[0]*n
        self.end_time=[0]*n
        self.time=0
        self.time_stamps=[[0,0]]*n

    def addEdge(self,u,v):
        self.dict[u].append(v)
    
    def dfs(self,u):
        self.color[u]='grey'
        self.start_time[u]=self.time
        self.time+=1
        print(u)
        for i in self.dict[u]:
            if self.color[i]=='white':
                self.dfs(i)
        self.color[u]='black'
        self.end_time[u]=self.time
        self.time+=1
        self.time_stamps[u]=[self.start_time[u],self.end_time[u]]
    
    
    def time_stamp(self):
        for i in range(0,self.vertices):
            if self.color[i]=='white':
                self.dfs(i)
        print(self.time_stamps)

    def decreasing_time(self):
        for i in range(0,self.vertices):
            max1=max(self.end_time)
            idx=self.end_time.index(max1)
            self.end_time[idx]=-1
            print(idx)

    
g=graph(5)
g.addEdge(0,4)
g.addEdge(0,2)
g.addEdge(2,3)
g.addEdge(1,4)
g.addEdge(2,4)
g.dfs(0)
g.time_stamp()
g.decreasing_time()