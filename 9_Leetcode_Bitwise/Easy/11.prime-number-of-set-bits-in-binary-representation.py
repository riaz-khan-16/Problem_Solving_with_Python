# 11. [Prime Number of Set Bits in Binary Representation]
#(https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/)

def count_1(n):
        count=0
        for i in range(22):
            bit=(n>>i)&1
            if bit==1:
                count=count+1
        return count  
def is_prime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
        return True
    else:
        return False   


def f(a,b):
   c=0
   for i in range(a,b+1):
      x=count_1(i)
      if is_prime(x):
          c=c+1
   return c       
          



print(f(10,15))

