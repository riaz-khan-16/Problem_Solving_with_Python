# Rotate Array
# (https://leetcode.com/problems/rotate-array/)
nums = [1,2,3,4,5,6,7] 
k = 3
l=len(nums)-1
for i in range(k):
    x=nums[l]
    nums.pop(l)
    nums.insert(0,x)
print(nums)

#Time Limit exceed