# https://leetcode.com/problems/majority-element/

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
nums = [3,3,4]

def FindMajority(arr):
    # find the unique set
    uniq=[]
    for i in arr:
        if i not in uniq:
             uniq.append(i)
    return uniq       

x=FindMajority(nums) 
print(x)     

for i in x:
    mj=0
    if nums.count(i)> mj:
       n=i
       print(n)




        

