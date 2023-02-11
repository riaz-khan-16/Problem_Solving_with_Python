# 13. [Largest Perimeter Triangle](https://leetcode.com/problems/largest-perimeter-triangle/)


# 976. Largest Perimeter Triangle
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

# Example 1:

# Input: nums = [2,1,2]
# Output: 5

# Brute Force
# nums = [2,1,2]

# def istrianglePossible(a,b,c):
#        if a+b>c and a+c>b and b+c>a:
#              return True
#        else:
#         return False      
    
# m=0
# for i in range(0,len(nums)-1):
#        a=nums[i]
#        for j in range(i+1,len(nums)-1):
#          b=nums[j]
#          for k in range(j+1,len(nums)):
#             c=nums[k]
#             if istrianglePossible(a,b,c) and m<a+b+c:
#                 m=a+b+c
# print(m)                


# optimize

nums =[2,1,2]

def findmax(nums):
    def istrianglePossible(a,b,c):
        if a+b>c and a+c>b and b+c>a:
                return True
        else:
            return False      
        
   
    nums.sort()
    l=len(nums)
    max=0
    for i in range(l-1,1,-1):
        a=nums[i]
        b=nums[i-1]
        c=nums[i-2]
        if istrianglePossible(a,b,c) and max<a+b+c:
            max=a+b+c
      
    return max
print(findmax(nums))    
