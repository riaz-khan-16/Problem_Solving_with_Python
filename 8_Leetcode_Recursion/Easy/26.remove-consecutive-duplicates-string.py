# 25. [Remove consecutive duplicate characters from a string.]
#(https://www.geeksforgeeks.org/remove-consecutive-duplicates-string/) GFG


a= 'aaaaabbbbb'

#Using Brute force
def find(a):
    b=[a[0]]
    for i in range(len(a)-1):
        
        if a[i]==a[i+1]:
            pass
        else:
            b.append(a[i+1])
        return b
#Using Recursion

def f(x,y):
    if len(y)==0:
        print(x)
        return
    if len(x)>=1 and  x[-1]==y[0]:
        f(x,y[1:])
    else:
         x=x+y[0]
         f(x,y[1:])


f('',a)        
    




