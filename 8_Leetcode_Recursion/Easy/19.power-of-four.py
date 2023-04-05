#18. [Power of Three](https://leetcode.com/problems/power-of-four/) leetcode


def f(n):

    if n==1:
        return True
    if n<1:
        return False
    
    return f(n/4)
print(f(64))