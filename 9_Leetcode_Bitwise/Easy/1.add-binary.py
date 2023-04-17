# 1. [Add Binary](https://leetcode.com/problems/add-binary/)

a = "1"
b = "1"

def binary_to_decimal(n):
    ans=0
    b=1
    while n>0:
        last=n%10
        n=n//10
        ans=ans+last*b
        b=b*2
    return ans
    
def decimal_to_binary(n):
    ans=''
    while n>0:
        last=n%2
        n=n//2
        ans=str(last)+ans
    return ans

def add(a,b):
    a=int(a)
    a=binary_to_decimal(a)
    b=int(b)
    b=binary_to_decimal(b)
    r=a+b
    return decimal_to_binary(r)
print(add(a,b))




