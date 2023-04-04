#15. [Check Prime or not](https://www.geeksforgeeks.org/recursive-program-prime-number/) GFG


def f(x,i):
    if x==2:
        return True
    if x<2:
        return True
    if x%i==0:
        return False
    if i*i>x:
        return True
    else:
         return f(x,i+1)
print(f(17,2))