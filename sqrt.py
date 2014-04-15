def sqrt(x):
        if x<0:
            return None
        if x==0:
            return 0
        if x==1:
            return 1
        val=x
        while True:
            last=val
            val = (val + x / val) * 0.5
            if abs(val-last)<1e-9:
                break
        return int(val)
