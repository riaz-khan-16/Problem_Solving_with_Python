#3. [Reverse Bits](https://leetcode.com/problems/reverse-bits/)

n =1001000001011110101101
   

re=0
for i in range(32):
    
    bit=(n>>i)&1
    re=re|(bit<<(32-i))
print(re)    

   








