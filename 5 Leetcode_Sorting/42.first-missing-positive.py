
## **Hard**

#1. [First missing Positive](https://leetcode.com/problems/first-missing-positive/)

nums=[1,2,3,5]
nums.sort()
res = 1
for num in nums:
    if num == res:
        res += 1
print(res)