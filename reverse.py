class Solution:
    # @return an integer
    def reverse(self, x):
        x=str(x)
        new=''
        for i in range (len(x)-1, 0, -1):
            new=new+x[i]
        if x[0]=='-':
            return -int(new)
        else:
            return int(new+x[0])
