# 13. [Number of Steps to Reduce a Number to Zero]
#(https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)


n=14

c=0
while n>0:
    if n%2==0:
        n=n/2
        c=c+1
    else:
        n=n-1
        c=c+1
print(c)        
