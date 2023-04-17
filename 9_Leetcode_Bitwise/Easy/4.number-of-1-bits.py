# 4. [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

n =1001000001011110101101
   


count=0
for i in range(22):
    
    bit=(n>>i)&1
    if bit==1:
        count=count+1
print(count)    