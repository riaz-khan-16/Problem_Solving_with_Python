# 9. [Length of string using Recursion](https://www.geeksforgeeks.org/program-for-length-of-a-string-using-recursion/) GFG


x='abcdkdlnvfkillljhhn'

def findLength(x):
    if x=='':
          return 0
    return 1+findLength(x[1:])
print(findLength(x))