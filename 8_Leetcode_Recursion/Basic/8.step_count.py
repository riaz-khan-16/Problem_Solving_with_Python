x=14

def fin(x,c):
    if x==0:
        return c
    if x%2==0:
        x=x/2
        return fin(x,c+1)
    else:   
        x=x-1
        return fin(x,c+1)
          
print (fin(x,0) )  
