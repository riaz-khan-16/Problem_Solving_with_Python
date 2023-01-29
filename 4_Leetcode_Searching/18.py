# [Find First and Last Position of Element in Sorted Array]
# (https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)


# Given an array of integers nums sorted in non-decreasing order, find the starting and 
# ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# nums = [5,7,7,8,8,8,1,1,3,10]
# target = 8

#Try with linear search
# def find1stIndex(nums,target):
#     for i in range(len(nums)):
#         if nums[i] ==target:
#             return i
# def findLastIndex(nums,target):
#     for i in range(len(nums)-1,-1,-1):
#         if nums[i] ==target:
#             return i    


nums = [5,7,7,8,8,10]
target = 8

nums = [5,7,7,8,8,10]
target = 6
#try with binary search

nums = [1]
target = 1
nums =[1,2,3]
target = 3
nums =[1,2,2]
target = 2


def findFI(nums,target):
    start=1
    end=len(nums)

    if target not in nums:
        return -1
    if len(nums)==1:
        return 0
    if  len(nums)==2:  
        if nums[0]==target:
            return 0
        else:
            return 1 
    if nums[0]==target:
        return 0    
    while start+1<end:
        mid=(start+end)//2
        if nums[mid]==target and nums[mid-1]<target:
            return mid
        if nums[mid]>target or nums[mid]==target:
            end=mid
        if nums[mid]<target:
            start=mid 
    return start


def findLI(nums,target):
    start=0
    end=len(nums)-1

    if target not in nums:
        return -1
    if len(nums)==1:
        return 0
    if  len(nums)==2:  
        if nums[1]==target:
            return 1
        else:
            return 0  
            
    while start+1<end:
        mid=(start+end)//2
        if nums[mid]==target and nums[mid+1]>target:
            return mid
        if nums[mid]>target:
            end=mid
        if nums[mid]<target or nums[mid]==target:
            start=mid 
    return start+1


if nums.count(target)==1:
    print(findFI(nums,target),findFI(nums,target))
print(findFI(nums,target))      
print(findLI(nums,target))  

