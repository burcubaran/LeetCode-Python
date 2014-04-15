class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if x==0:
            return 0
        if n==1:
            return x
        if n==0:
            return 1
        
        if n<0:
            n=n*(-1)
            x=(1/float(x))
        if n%2==1 and n-1>0:
            return self.pow(x,n-1)*x
        elif n%2==0:
            return self.pow(x*x,n//2)
