class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing

        
    def merge(self, A, m, B, n):
        if not A:
            A=A+B
            return A
        elif not B:
            return A
        else:
            k=m-1
            for i in range(n-1, -1, -1):
                A=self.helper(B[i], A)
            return A
            
        
    def helper(self, element, alist):
        i=len(alist)-1
        alist.append(element)
        position=len(alist)-1
        found=True
        while i>0 and found:
            if alist[i]>=element:
                temp=alist[position]
                alist[position]=alist[i]
                alist[i]=temp
                position=i
                i=i-1
            else:
                found=False
        return alist
