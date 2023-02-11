# https://leetcode.com/problems/third-maximum-number/


# Given an integer array nums, return the third distinct maximum number in this array.
#  If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1

# Example 2:

# Input: nums = [1,2]
# Output: 2


# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1


nums = [3,3,4,3,4,3,0,3,3]

def sort(a):
    for i in range(len(a)):
        for j in range(0,len(a)-1-i):
            if a[j]>a[j+1]:
                #swap
                 temp=a[j]
                 a[j]=a[j+1]
                 a[j+1]=temp
    return a            
         
nums=sort(nums)
first=nums[len(nums)-1]

def findSecond(nums):
    for i in range(len(nums)-2,-1,-1):
        if nums[i]<first:
            second=nums[i]
            return second
second=findSecond(nums)

def findThird(nums):
    for i in range(len(nums)-2,-1,-1):
            if nums[i]<second:
                third=nums[i]
                return third

third=findThird(nums)


if third in nums:
        print (third)
else:     
        print(first)



# allternative O(n)

def thirdMax(nums):
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)

      






