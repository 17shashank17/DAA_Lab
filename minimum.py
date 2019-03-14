def Minimum(arr,low,high):
    if low==high:
        return arr[low]
    mid=(low+high)//2
    return min(Minimum(arr,low,mid),Minimum(arr,mid+1,high),cross_Min(arr,low,mid,high))

def cross_Min(arr,low,mid,high):
    left=[]
    right=[]

    for i in range(low,mid+1):
        left.append(arr[i])

    for j in range(mid+1,high+1):
        right.append(arr[j])

    min1,min2=left[0],right[0]
    for i in range(1,len(left)):
        if min1>left[i]:
            min1=left[i]

    for j in range(1,len(right)):
        if min2>right[j]:
            min2=right[j]

    return min(min1,min2)

arr=[4,2,6,1,8,5,9,10]
print(Minimum(arr,0,len(arr)-1))