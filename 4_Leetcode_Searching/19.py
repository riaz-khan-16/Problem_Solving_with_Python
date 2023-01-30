#  Single Element in a Sorted Array
# https://leetcode.com/problems/single-element-in-a-sorted-array/

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10

nums = [1,1,2,3,3,4,4,8,8]

def find1(nums):
    start=1
    end=len(nums)-1
    while start+1<end:
        mid=(start+end)//2
        if nums[mid]>nums[mid-1] and nums[mid]<nums[mid+1]:
            return mid
        if  nums[mid]<nums[mid+1]:
                  
        if nums[mid]>nums[mid+1]:



