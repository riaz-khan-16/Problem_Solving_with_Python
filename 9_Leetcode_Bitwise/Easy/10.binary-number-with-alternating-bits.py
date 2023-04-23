# 10. [Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits/)


n=11


def f(n):
    a=n&1
    n=n>>1
    while n>0:
        b=n&1
        if b==a:
            return False
        n=n>>1
        a=b
    return True
print(f(n))    
    

