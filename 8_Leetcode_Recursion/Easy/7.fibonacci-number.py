#7. [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) leetcode

n=4

def fibo(n):
    if n<2:
        return n
    return fibo(n-1)+fibo(n-2)

print(fibo(n))