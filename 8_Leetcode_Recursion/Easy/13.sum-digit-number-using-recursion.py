#13. [Sum of digit of a number using Recursion](https://www.geeksforgeeks.org/sum-digit-number-using-recursion/) GFG




def f(num):

    num=str(num)
    if len(num)==0:
        return 0
    x=int(num[0])+int(f(num[1:]))
    return x

print(f(123))

def f1(num):

    if num==0:
        return 0
    x=num%10+f1(num//10)
    return x

print(f1(1234))
