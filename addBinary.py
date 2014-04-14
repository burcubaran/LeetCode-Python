class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        alist=[c for c in a]
        blist=[c for c in b]
        carry=0
        new=''
        while len(alist)!=0 or len(blist)!=0:
            if alist and blist:
                num=int(alist.pop())+int(blist.pop())+carry
            elif alist:
                num=int(alist.pop())+carry
            elif blist:
                num=int(blist.pop())+carry
            carry=num//2
            new=str(num%2)+new
        
        if carry==1:
            new='1'+new
        return new
        
