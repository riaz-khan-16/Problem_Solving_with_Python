#13. [Sum of digit of a number using Recursion](https://www.geeksforgeeks.org/sum-digit-number-using-recursion/) GFG

a=123456


def f(num):

    num=str(num)
    if len(num)==0:
        return 0
    x=int(num[0])+int(f(num[1:]))
    return x

print(f(123))