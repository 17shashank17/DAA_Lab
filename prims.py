from collections import defaultdict
class heap:
    def __init__(self):
        self.heap=[]
        self.top=0

    def insert(self,x):
        if self.heap==[]:
            self.heap.append(x)
        else:
            self.heap.append(x)
            self.top+=1
        i=self.top
        while True:
            if i%2==0:
                p=(i-2)//2
            else:
                p=(i-1)//2
            if p<0:
                return
            if self.heap[p]<self.heap[i]:
                break
            else:
                self.heap[p],self.heap[i]=self.heap[i],self.heap[p]
                i=p

    def heapify(self,i):
        p=i
        r=2*i+2
        l=2*i+1
        if l>=len(self.heap) and r>=len(self.heap):
            return
        elif l<len(self.heap) and r>=len(self.heap):
            if self.heap[l]<self.heap[p]:
                self.heap[p],self.heap[l]=self.heap[l],self.heap[p]
                self.heapify(l)
        else:
            if self.heap[l]>self.heap[p] and self.heap[r]>self.heap[p]:
                return
            else:
                if self.heap[l]<self.heap[p]:
                    self.heap[l],self.heap[p]=self.heap[p],self.heap[l]
                    self.heapify(l)
                elif self.heap[r]<self.heap[p]:
                    self.heap[r],self.heap[p]=self.heap[p],self.heap[r]
                    self.heapify(r)

    def minimum(self):
        return self.heap[0]
    
    def extract_min(self):
        x=self.heap[0]
        self.heap[0]=self.heap[len(self.heap)-1]
        self.heap.pop()
        self.heapify(0)
        return x

    def build_heap(self,arr):
        self.heap=[]
        for i in range(len(arr)):
            self.heap.append(arr[i])
        self.top=len(arr)-1
        for i in range(((len(arr))//2)-1,-1,-1):
            self.heapify(i)

    def updatePriority(self,old,new):
        if old==new:
            return
        elif old not in self.heap:
            return
        else:
            j=self.heap.index(old)
            self.heap[j]=new
            self.heapify(j)
        i=0
        while i<=j:
            self.heapify(i)
            i+=1
    
    def isEmpty(self):
        if len(self.heap)==0:
            return True
        return False 

    
    def printt(self):
        print(self.heap)

class graph:
    def __init__(self,n):
        self.graphs=defaultdict(list)
        self.distances=[[-1 for i in range(n) ] for s in range(n) ]
        self.size=n

    def addEdge(self,u,v,d):
        self.graphs[u].append([v,d])

    def Prims(self):
        h=heap()
        dist=[float('inf')]*self.size
        pred=[None]*self.size
        dist[0]=0
        h.build_heap(dist)
        list1=[]
        while True:
            if h.isEmpty():
                break
            else:
                u=h.extract_min()
                for v in self.graphs[u]:
                    w,d=int(v[0]),int(v[1])
                    if dist[w]>d:
                        list1.append([u,w])
                        temp=dist[w]
                        dist[w]=d
                        pred[w]=u
                        h.updatePriority(temp,dist[w])
        print(pred)
        print(list1)



def main():
    g=graph(4)
    g.addEdge(0,1,5)
    g.addEdge(0,2,3)
    g.addEdge(3,0,6)
    g.addEdge(1,3,7)
    g.addEdge(2,1,4)
    g.addEdge(2,3,5)

    g.Prims()

if __name__=='__main__':
	main()

