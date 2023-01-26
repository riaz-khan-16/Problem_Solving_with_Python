# Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)


# Given two integer arrays nums1 and nums2, return an array of their intersection. 

# Each element in the result must appear as many times as it shows in both arrays and 
# you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# nums1 = [4,9,5], nums2 = [9,4,9,8,4]

nums1 = [4,9,5,2,1,1,3]
nums2 = [9,4,9,8,4]
a=[]

for i in nums2:
    if i in nums1:
        a.append(i)
        nums1.remove(i)

print(a)        