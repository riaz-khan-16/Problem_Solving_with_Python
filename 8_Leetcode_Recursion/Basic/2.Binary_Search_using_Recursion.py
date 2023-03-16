a=[1,2,5,7,9,10,15,16,21]
target=21

b=0
e=len(a)-1


def findTarget(a,target,b,e):
    m=(b+e)//2
    if a[m]==target:
        return m
    
    if a[m]<target:
        return findTarget(a,target,m+1,e)
    else:
        return findTarget(a,target,b,m-1)

print(findTarget(a,target,b,e))   