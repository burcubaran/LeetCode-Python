class Solution:
    # @return a string
    def seq(self,a):
        last=a[0]
        k=1
        new=''
        for i in range(1,len(a)):
            if a[i]==last:
                k+=1
            else:
                new=new+str(k)+last
                k=1
            last=a[i]
        new=new+str(k)+last
        return new
        
        
    def countAndSay(self, n):
        if n==1:
            return '1'
        else:
            return self.seq(self.countAndSay(n-1))
