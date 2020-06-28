array = []

def Josephus(darray,starting,n):
    if len(darray) ==1:
        return darray
    elif n == 13:
        del darray[n % len(darray)]
        if starting == len(darray)-1:
            return Josephus(darray,0,n+1)
        return Josephus(darray,starting+1,n+1)
    else:
        if starting == len(darray)-1:
            return Josephus(darray,0,n+1)
        return Josephus(darray,starting+1,n+1)

        
        
    