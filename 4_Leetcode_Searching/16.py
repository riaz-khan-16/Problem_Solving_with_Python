#[Special Array With X Elements Greater Than or Equal X]
# (https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x


# You are given an array nums of non-negative integers.
#  nums is considered special if there exists a number x such that 
#  there are exactly x numbers in nums that are greater than or equal to x.

# Notice that x does not have to be an element in nums.

# Return x if the array is special, otherwise, return -1. 
# It can be proven that if nums is special, the value for x is unique.

nums = [3,5]
def findgreaterthani(n,arr):
    count=0
    for i in arr:
        if i>=n:
            count=count+1
    return count






for i in range(len(nums)+1):
    if i==findgreaterthani(i,nums):
        print(i)
        
     


       