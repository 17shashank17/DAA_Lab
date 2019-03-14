def partition(arr,x):
    a=[]
    for i in range(len(arr)):
        if arr[i]<x:
            a.append(arr[i])

    a.append(x)
    for i in range(0,len(arr)):
        if arr[i]>=x:
            a.append(arr[i])

    return a.index(x)

#def find_approx_med(arr):
 #   if len(arr)<5:


def Select(arr,low,high,k):
    #x=find_approx_med(arr)
    x=arr[k]
    i=partition(arr,x)
    if i==k:
        return x
    elif i>k:
        return Select(arr[low:i],low,high,k)
    else:
        return Select(arr[i:high+1],low,high,k-i-1)

arr=[1,4,6,3,8,7,2]
print(Select(arr,0,len(arr)-1,6))