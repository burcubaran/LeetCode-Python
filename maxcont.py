def maxcont(alist):
    maxsum=alist[0]
    sum=alist[0]
    for i in range(1,len(alist)):
        if alist[i] >= sum+alist[i]:
            sum=alist[i]
        else:
            sum=sum+alist[i]
        if sum>maxsum:
            maxsum=sum
    return maxsum
