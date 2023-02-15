# . [3Sum Closest](https://leetcode.com/problems/3sum-closest/)


# Given an integer array nums of length n and an integer target, 
# find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 


nums = [-1,2,1,-4]
target = 1

# Alogorithm:
#           1.Sort the array
#           2.sum=nums[0]+nums[1]+nums[2]
#           3.Take a number by a for loop:
#                 i. a=nums[i]
#                 ii. find the other two using two pointer
#  

def threeSumClosest( num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result

