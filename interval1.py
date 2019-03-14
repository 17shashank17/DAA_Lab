from collections import defaultdict

def mergeSort(arr,low,high):
    if low>=high:
        return
    else:
        mid=(low+high)//2
        mergeSort(arr,low,mid)
        mergeSort(arr,mid+1,high)
        merge(arr,low,mid,high)
        return arr

def merge(arr,low,mid,high):
    left=[]
    right=[]
    for i in range(low,mid+1):
        left.append(arr[i])

    for j in range(mid+1,high+1):
        right.append(arr[j])

    i,j=0,0
    k=low
    while i<len(left) and j<len(right):
        if left[i][1]>right[j][1]:
            arr[k]=right[j]
            j+=1
        else:
            arr[k]=left[i]
            i+=1
        k+=1

    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    
def interval_Scheduling_I(arr):
    arr=mergeSort(arr,0,len(arr)-1)
    interval=[]
    interval.append(arr[0])
    finish=arr[0][1]
    start=0
    for i in arr:
        if i==arr[0]:
            continue
        else:
            start=i[0]
            if start>=finish:
                interval.append(i)
                finish=i[1]
    return interval

def interval_Scheduling_II(arr):
    arr=mergeSort(arr,0,len(arr)-1)
    groups=defaultdict(list)
    list1=[]
    start=0
    flag=0
    finish=arr[0][1]
    list1.append(finish)
    groups[0].append(arr[0])
    for i in arr:
        if i==arr[0]:
            continue

        for j in range(len(groups)):
            if i[0]>=list1[j]:
                groups[j].append(i)
                list1[j]=i[1]
                flag=1
                break
        if flag==0:
            groups[j+1].append(i)
            list1.append(i[1])
        flag=0
    for i in range(0,len(groups)):
        print("Group",i+1,":",groups[i])





arr=[[1,2],[2,3],[4,7],[5,9],[2,7],[3,8],[8,10]]
interval_Scheduling_II(arr)


