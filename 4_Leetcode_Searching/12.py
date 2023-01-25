# https://leetcode.com/problems/intersection-of-two-arrays/

# Given two integer arrays nums1 and nums2, return an array of their intersection.
#  Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.


#linear search
nums1 = [4,9,5,5] 
nums2 = [9,4,9,8,4]

nums1 = [1,2,2,1]
nums2 = [2,2]

Inter=[]
for i in nums2:
    if i in nums1:
        Inter.append(i)
for i in nums1:
    if i in nums2:
        Inter.append(i)  
print(Inter )         

       
       



 