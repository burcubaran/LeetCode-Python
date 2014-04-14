class Solution:
    # @param s, a string
    # @return a boolean
    
    
    def isPalindrome(self, s):
        alist="""!&,.;:?'@#$%^*()-"`~ """
        newlist=[]
        for i in s:
            if i not in alist:
                newlist.append(i)
        i=0
        result=True
        j=len(newlist)-1
        if len(newlist)>1:
            while i<=j and result:
                    if newlist[i].lower()==newlist[j].lower():
                        i=i+1
                        j=j-1
                    else:
                        result=False
        return result
