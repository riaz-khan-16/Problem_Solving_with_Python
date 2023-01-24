# Search Insert Position
# https://leetcode.com/problems/search-insert-position/

# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

nums =[1,3,5,6]
target = 7
start= 0
end=len(nums)
def findtheIndex(nums,target,start,end):
    while start+1<end:
        mid=(start+end)//2
        if nums[mid]==target:
            return mid
        elif  nums[mid]>target: 
            end=mid
        else:
            start=mid  
    return start+1
if nums[0]>=target:
    print(0 )  
   
        
print(findtheIndex(nums,target,start,end))    