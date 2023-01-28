# [Find First and Last Position of Element in Sorted Array]
# (https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)


# Given an array of integers nums sorted in non-decreasing order, find the starting and 
# ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
nums = [5,7,7,8,8,10]
target = 8

#Try with linear search
# def find1stIndex(nums,target):
#     for i in range(len(nums)):
#         if nums[i] ==target:
#             return i
# def findLastIndex(nums,target):
#     for i in range(len(nums)-1,-1,-1):
#         if nums[i] ==target:
#             return i    



    


#try with binary search

def find1stIndex(nums,target):
    start=1
    end=len(nums)
    while start+1<end:
        mid=(start+end)//2
        if nums[mid]==target and nums[mid-1]<target:
            return mid
        elif nums[mid]>target:
            end=mid
        else:
            start=mid
    if nums[0]==target:
        return 0


def findlastIndex(nums,target):
    start=0
    end=len(nums)-1
    while start+1<end:
        mid=(start+end)//2
        if nums[mid]==target and nums[mid+1]>target:
            return mid
        elif nums[mid]>target:
            end=mid
        else:
            start=mid
    if len(nums)==1:
        return 0







print(find1stIndex(nums,target))  
print(findlastIndex(nums,target))   