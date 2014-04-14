class Solution:
    # @return a boolean
    def thesame(self,x,y):
        alist1='{[('
        alist2='}])'
        if x==alist1[0] and y==alist2[0]:
            return True
        elif x==alist1[1] and y==alist2[1]:
            return True
        elif x==alist1[2] and y==alist2[2]:
            return True
        else:
            return False
    
    def isValid(self, s):
        parlist=[]
        alist1='{[('
        alist2='}])'
        found=True
        i=0
        while i<len(s) and found:
            if s[i] in alist1:
                parlist.append(s[i])
            else:
                if parlist==[]:
                    found=False
                else:
                    x=parlist.pop()
                    found=self.thesame(x,s[i])
            i=i+1
        if parlist==[] and found:
            return True
        else:
            return False
