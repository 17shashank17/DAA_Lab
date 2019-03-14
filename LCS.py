a=input()
b=input()
al=list(a)
bl=list(b)
la=len(al)
lb=len(bl)
l=[]
c=[[0 for i in range(lb+1)] for s in range(la+1) ]
for i in range(0,lb):
    for k in range(0,la):
        if al[k]==bl[i]:
            c[k+1][i+1]=1+c[k][i]
            #l.append(al[k])
        else:
            c[k+1][i+1]=max(c[k][i+1],c[k+1][i])
for i in range(lb+1):
    for k in range(la+1):
        print(c[k][i],end=" ")
    print(" ")



                    
