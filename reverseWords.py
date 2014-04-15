    def reverseWords(self, s):
        if len(s)==0:
            return ""
        alist=s.split()
        output=[]
        
        if len(alist)>1:
            for i in range(len(alist)-1):
                output.append(alist[i])
                output.append(" ")
            output.append(alist[len(alist)-1])
        else:
            output +=alist
        new=''
        for i in range(len(output)):
            new=new+output.pop()
            
        return new
