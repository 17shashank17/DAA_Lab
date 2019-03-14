from collections import defaultdict

class graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.dict=defaultdict(list)
        self.count=[0]*vertices
        self.stack=[]

    def addEdge(self,u,v):
        self.dict[u].append(v)
        self.count[v]+=1

    def zero_indegree(self):
        for i in range(0,self.vertices):
            if self.count[i]==0:
                self.stack.append(i)
        print(self.stack)

    def print_stack(self):
        print(self.stack)

    def topoplogical_sort(self):

        while len(self.stack) != 0:
            x=self.stack.pop()
            self.count[x]=-5
            #print(x)
            for j in self.dict[x]:
                self.count[j]-=1
                if self.count[j]==0:
                    self.stack.append(j)
        
            

g=graph(7)
g.addEdge(0,1)
g.addEdge(1,4)
g.addEdge(4,3)
g.addEdge(6,4)
g.addEdge(6,5)
g.addEdge(2,5)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(1,3)
g.addEdge(5,3)
#g.prinnt()
g.zero_indegree()
g.topoplogical_sort()