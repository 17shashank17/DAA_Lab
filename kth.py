def select(A, B, k):
    if k >= len(A) + len(B):
        raise IndexError('list index out of range')
    while k > 0:
        m = (k-1)//2
        if m >= len(A):
            B = B[m+1:]
        elif m >= len(B) or A[m] <= B[m]:
            A = A[m+1:]
        else:
            B = B[m+1:]
        k -= m + 1
    if len(A) == 0:
        return B[0]
    if len(B) == 0:
        return A[0]
    return min(A[0], B[0])

A=[2,5,7,8]
B=[1,3,4,9]
k=7
print(select(A,B,k))

