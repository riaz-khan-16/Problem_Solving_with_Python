# 16. [Sum of Natural numbers using Recursion]
#(https://www.geeksforgeeks.org/sum-of-natural-numbers-using-recursion/) GFG

n=5

def f(n):
    if n==0:
        return 0
    x=n+f(n-1)
    return x

print(f(5))