class Solution:
    # @return an integer
    
    def romanToInt(self, s):
        d={}
        d['I']=1
        d['IV']=4
        d['V']=5
        d['IX']=9
        d['X']=10
        d['XL']=40
        d['L']=50
        d['XC']=90
        d['C']=100
        d['CD']=400
        d['D']=500
        d['CM']=900
        d['M']=1000
        sum=0
        i=0
        while i<len(s):
            if i+1<len(s) and s[i]+s[i+1] in d:
                sum=sum+d[s[i]+s[i+1]]
                i=i+2
            else:
                sum=sum+d[s[i]]
                i=i+1
                
        return sum
