# 12. [Binary Gap](https://leetcode.com/problems/binary-gap/)

    
def f(N):
    l = bin(N)
    p1, p2 = 0, 0
    dtc = 0

    for i in range(2,len(l)):
        if l[i]=='1':
            if p1==0:
                p1=i
            else:
                p2=i
                dtc=max(p2-p1,dtc)
                p1 = p2
    return dtc

print(f(22))