# Given an array of integers nums which is sorted in ascending order,
#  and an integer target, write a function to search target in nums.
#   If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4



nums = [-1,0,3,5,9,12]
target = 9



def find(arr,target):
       start=0
       end=len(arr)
       while start+1<end:
           mid=(start+end)//2
           if arr[mid]==target:
               return mid
           elif   arr[mid]>target:  
               end=mid
           else:
               start=mid
       return -1         


r=find(nums,target)
print(r)
