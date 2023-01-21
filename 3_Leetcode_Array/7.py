#Number of Good Pairs---> leetcode(1512)
# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


nums = [1,1,1,1]
b=0
for i in range(len(nums)):
    a=0
    for j in range(i+1,len(nums),1):
        if nums[i]==nums[j]:
            a=a+1
    b=b+a 
print(b)    