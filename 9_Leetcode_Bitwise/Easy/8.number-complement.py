#8. [Number Complement](https://leetcode.com/problems/number-complement/)


num = 2

def binary_to_decimal(n):
    ans=0
    b=1
    while n>0:
        last=n%10
        n=n//10
        ans=ans+last*b
        b=b*2
    return ans

def find_Complement(num):
    ans=''
    while num>0:
        c=(num & 1)^1
        ans=str(c)+ans
        num=num>>1
    print(binary_to_decimal(int(ans)))    
    
   
find_Complement(num)   