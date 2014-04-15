def partition(alist):
    pivot=alist[0]
    left=1
    right=len(alist)-1
    
    done=False
    while not done:
        while left<=right and  alist[left]<=pivot:
            left=left+1
            
        while left<=right and alist[right]>=pivot:
            right=right-1
            
        if right<left:
            done=True
        else:
            temp=alist[left]
            alist[left]=alist[right]
            alist[right]=temp
            
    temp=alist[0]
    alist[0]=alist[right]
    alist[right]=temp
    
    return right
    
    
    
def findklargest(alist, k):
    
    p=partition(alist)
    leftlist=alist[:p]
    rightlist=alist[p+1:]
    
    if len(rightlist)==k-1:
        return alist[p]
    
    elif len(rightlist)>=k:
        return findklargest(rightlist,k)
    else:
        return findklargest(leftlist, k-(len(rightlist)+1))
