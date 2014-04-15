def allperm(alist):
    if len(alist)<=1:
        return [alist]
    
    #get all permutations of length N-1
    perms=allperm(alist[1:])
    
    char=alist[0]
    output=[]
    
    #iterate over all permutations of length N-1
    for perm in perms:
        for k in range(len(perm)+1):
            output.append(perm[:k]+[char]+perm[k:])
    return output
