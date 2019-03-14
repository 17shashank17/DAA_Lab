def majority(arr,low,high):
    if len(arr)==2:
        if arr[0]==arr[1]:
            return arr[0]
        else:
            return -1

    elif len(arr)==1:
        return arr[0]

    mid=(low+high)//2
    x1=majority(arr,low,mid)
    x2=majority(arr,mid+1,high)

    if x1==-1 and x2>0:
        return x2

    elif x2==-1 and x1>0:
        return x1

    elif x1==x2:
        return x1

    else:
        return -1

arr=[6,3,3,3,3,2]
print(majority(arr,0,len(arr)-1))