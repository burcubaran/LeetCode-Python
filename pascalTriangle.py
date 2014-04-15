class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        res=[]
        
        if numRows>=1:
            res.append([1])
        if numRows>=2:
            res.append([1,1])
        
        for i in range(3, numRows+1):
            cur=[1]
            prev=res[-1]
            for i in range(1, i-1):
                cur.append(prev[i-1]+prev[i])
            cur.append(1)
            res.append(cur)
            
        return res
