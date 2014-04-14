def singleNumber(self, A):
        d=dict()
        sum=0
        for i in A:
            if i in d:
                sum=sum-i
            else:
                d[i]=i
                sum=sum+i
        return sum
