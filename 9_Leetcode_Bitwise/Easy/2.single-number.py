# 2. [Single Number](https://leetcode.com/problems/single-number/)

arr=[1,1,3,3,5,6,6]

ans=0
for i in arr:
    element=i
    ans=ans^element
print(ans)    

