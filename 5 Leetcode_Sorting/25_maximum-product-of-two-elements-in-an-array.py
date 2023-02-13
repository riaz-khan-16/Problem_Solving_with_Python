
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Given the array of integers nums, you will choose two different indices i and j of that array. 
# Return the maximum value of (nums[i]-1)*(nums[j]-1).
 


# Input: nums = [3,4,5,2]
# Output: 12 

# Input: nums = [1,5,4,5]
# Output: 16

nums = [1,5,4,5]
nums.sort()

l=len(nums)-1
print(nums)
x=nums[l]-1
y=nums[l-1]-1
print(x*y)