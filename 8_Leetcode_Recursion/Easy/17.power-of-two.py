# 17. [Power of Two](https://leetcode.com/problems/power-of-two/)


def f(n):

    if n==1:
        return True
    if n<1:
        return False
    
    return f(n/2)
print(f(3))
    
  

