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

nums = [1,1,2,2,3,3,4,4,6,6,7,8,8]
nums=[1,2,2,3,3]

#algoruithm


#boundary check
#If pair is started in even index ---> go right
#If pair is started in odd index ---> go left

# check the boundary
def checkBoundary(nums):
    l=len(nums)
    if nums[0]!=nums[1]:
        return nums[0]
    elif   nums[l-1]!=nums[l-2]:
        return nums[l-1]
   

# print(checkBoundary(nums))          

def pairStartIndex(nums,i):
      if nums[i]==nums[i-1]:
        return i-1
      elif  nums[i]==nums[i+1]:
        return i

# print(pairStartIndex(nums,12))

def isEven(i):
    if i%2==0:
        return True
    else:
        return False    


nums=[1,2,2,3,3]

def findUnique(nums):
     if len(nums)==1:
        return nums[0]
     #boundary Check   
     l=len(nums)
     if nums[0]!=nums[1]:
        return nums[0]
     elif   nums[l-1]!=nums[l-2]:
        return nums[l-1]
     # Binary check   
     s=0
     e=len(nums)
     while s+1<e:
        m=(s+e)//2
        if nums[m]!=nums[m-1] and nums[m]!=nums[m+1]:
            return nums[m]
        x= pairStartIndex(nums,m)
        if isEven(x):
            s=m
        if not isEven(x):
            e=m
     return nums[s+1]  

print(findUnique(nums))      

          



