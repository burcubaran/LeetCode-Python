class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        d={}
        sum=0
        for i in A:
            if i not in d:
                d[i]=[i]
                sum=sum+i
            else:    
                if len(d[i])==1:
                    sum=sum+i
                    d[i].append(i)
                elif len(d[i])==2:
                    sum=sum-(2*i)
                    
        return sum
