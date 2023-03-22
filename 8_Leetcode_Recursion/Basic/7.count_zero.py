x=10012302000000000



def countzero(x,c):

    if x==0:
        return c
    
    d=x%10
    if d==0:
        return countzero(x//10,c+1)
    else:
        return countzero(x//10,c)

print(countzero(x,0))