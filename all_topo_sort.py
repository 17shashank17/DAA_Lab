from collections import defaultdict
class graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.dict=[]
        self.count=[0]*vertices
        self.stack=[]

    def addEdge(self,u,v):
        self.dict[u].append(v)
        self.count[v]+=1

    def topological(self):
        for i in range(self.vertices):
            if self.count[i]==0:
                self.stack.append(i)

        while len(self.stack) !=0:
            x=self.stack.pop()
            print(x)
            for j in self.dict[x]:
                self.count[j]-=1
                if self.count[j]==0:
                    self.stack.append(j)
                    