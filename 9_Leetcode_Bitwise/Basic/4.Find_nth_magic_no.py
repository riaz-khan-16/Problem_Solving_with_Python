

#amazon question

def find(n):
    a=0
    b=5

    while n>0:
        l=n&1
        n=n>>1
        a=l*b
        b=b*5
    print(a)    

find(1)