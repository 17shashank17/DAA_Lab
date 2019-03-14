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
        self.stack=[]

    def addEdge(self,u,v):
        self.dict[u].append(v)

    def dfsv(self,u):
        self.color[u]='grey'
        self.start_time[u]=self.time
        self.time+=1
        for i in self.dict[u]:
            if self.color[i]=='white':
                self.dfs(i)
        self.color[u]='black'
        self.end_time[u]=self.time
        self.stack.append(u)
        self.time+=1
        self.time_stamps[u]=[self.start_time[u],self.end_time[u]]
        
    def dfs(self,u):
        self.color[u]='grey'
        self.start_time[u]=self.time
        self.time+=1
        print(u,end=" ")
        for i in self.dict[u]:
            if self.color[i]=='white':
                self.dfs(i)
        self.color[u]='black'
        self.end_time[u]=self.time
        self.stack.append(u)
        self.time+=1
        self.time_stamps[u]=[self.start_time[u],self.end_time[u]]
    
    
    def time_stamp(self):
        for i in range(0,self.vertices):
            if self.color[i]=='white':
                self.dfsv(i)
        #print(self.time_stamps)

    def graph_Transpose(self):
        gr=graph(self.vertices)
        for i in self.dict:
            for j in self.dict[i]:
                gr.addEdge(j,i)
        return gr

    def compute_Scc(self):
        self.dfsv(0)
        self.time_stamp()
        self.stack.sort()
        self.stack.reverse()
        print()
        gr=self.graph_Transpose()
        gr.color=['white']*self.vertices
        count=0
        while len(self.stack) != 0:
            u=self.stack.pop()
            if gr.color[u]=='white':
                gr.dfs(u)
                count+=1
                print()
        return count

g=graph(6)
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 1) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
g.addEdge(4,5)
g.addEdge(5,3)
print(g.compute_Scc())




