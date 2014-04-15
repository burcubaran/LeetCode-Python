class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if not points:
            return 0
        res=1
        for i in range(len(points)):
            d={'inf':0}
            samenumber=1
            for j in range(len(points)):
                if i != j:
                    if points[i].x==points[j].x and points[i].y!=points[j].y:
                        d['inf']+=1
                    elif points[i].x!=points[j].x:
                        k=1.0*(points[j].y-points[i].y)/(points[j].x-points[i].x)
                        if k in d:
                            d[k]+=1
                        else:
                            d[k]=1
                    else:
                        samenumber +=1
            res=max(res, max(d.values())+samenumber)
        return res
