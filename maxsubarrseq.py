#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    sum1=0
    sum2=0
    i=0
    flag=0
    for j in range(len(arr)):
        if arr[j]>=0:
            flag=1
    if flag==0:
        sum3=max(arr)
        return [sum3,sum3]
    k=0
    for s in range(len(arr)):
        if arr[s]<0:
            k=1
    if k==0:
        sum4=sum(arr)
        return [sum4,sum4]

    sum_seq=0
    for s in range(0,len(arr)):
        if arr[s]>=0:
            sum_seq+=arr[s]
            print(arr[s])
    print(sum_seq)
    i=0
    sum2=-(sys.maxint)-1
    while i<len(arr):
        sum1+=arr[i]
        if sum1<0:
            sum1=0
        elif sum2<sum1:
            sum2=sum1
    return [sum2,sum_seq]



if __name__ == '__main__':


    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        print(result)