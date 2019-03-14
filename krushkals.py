from collections import defaultdict
class node:
	def __init__(self,data=None):
		self.data=data
		self.parent=self
		self.rank=0
		self.child=[]

class Disjoint_Set_Adt:
	def __init__(self,vertices):
		self.vertices=vertices
		self.arr=[]

		pass

	def highest_ancestor(self,x):
		temp=self.arr[x]
		while temp != temp.parent:
			temp=temp.parent
		return temp


	def makeSet(self,x):
		temp=node(x)
		temp.parent=temp
		self.arr.append(temp)

	'''def findSet(self,x):
		temp=self.arr[x]
		while temp != temp.parent:
			temp=temp.parent
		return temp'''

	def findSet(self,x):
		temp=self.arr[x]
		if temp.parent != temp:
			j=self.arr.index(temp.parent)
			y=self.findSet(j)
			temp.parent=y
			return y
		return temp


	def union(self,x,y):
		rx=self.findSet(x)
		ry=self.findSet(y)

		if rx==ry:
			print("They are in same componenets")
		else:
			if rx.rank>ry.rank:
				ry.parent=rx
			elif rx.rank<ry.rank:
				rx.parent=ry
			else:
				rx.parent=ry
				ry.rank+=1

class graph:
    def __init__(self,vertices,edges):
        self.vertices=vertices
        self.dist=[]
        self.edges=edges
        self.T=Disjoint_Set_Adt(vertices)
        for i in range(vertices):
            self.T.makeSet(i)

    def addEdge(self,u,v,d):
        self.dist.append([u,v,d])
        

    def Krushkals(self):
        list1=[]
        S=graph(self.vertices,self.edges)
        self.dist =  sorted(self.dist,key=lambda item: item[2])
        for i in range(0,self.edges):
            u,v,d=self.dist[i]
            if self.T.findSet(u) != self.T.findSet(v):
                S.addEdge(u,v,d)
                list1.append([u,v])
                self.T.union(u,v)

        print(list1)
        S.prinnt()

    def prinnt(self):
        print(self.dist)



def main():
    g=graph(4,6)
    g.addEdge(0,1,5)
    g.addEdge(0,2,3)
    g.addEdge(3,0,6)
    g.addEdge(1,3,7)
    g.addEdge(2,1,4)
    g.addEdge(2,3,5)

    g.Krushkals()

if __name__=='__main__':
	main()


        

        



