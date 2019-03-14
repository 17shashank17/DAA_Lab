# This is for only positive number

#Recursive Solution


def subset(arr,n,sum):
    if sum==0:
        return True
    if n==0 and sum != 0:
        return False
    if arr[n-1]>sum:
        return subset(arr,n-1,sum)
    return subset(arr,n-1,sum) or subset(arr,n-1,sum-arr[n-1])

arr=[1,1,3,7,5]
m=8
print(subset(arr,len(arr),m))

#Dynamic Programming

