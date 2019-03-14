def sort_and_count_inversions(arr,low,high):
    if low>=high:
        return 0
    else:
        mid=(low+high)//2
        il=sort_and_count_inversions(arr,low,mid)
        il+=sort_and_count_inversions(arr,mid+1,high)
        il+=sort_and_count_split_inversions(arr,low,mid,high)
    return il

def sort_and_count_split_inversions(arr,low,mid,high):
    left=[]
    right=[]
    for i in range(low,mid+1):
        left.append(arr[i])

    for j in range(mid+1,high+1):
        right.append(arr[j])
    i,j=0,0
    count=0
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            count+=1
            k=len(left)-i-1
            count+=k
            j+=1
        else:
            i+=1
    return count

arr=[1,4,3,6,2,7,0,9]
print(sort_and_count_inversions(arr,0,len(arr)-1))