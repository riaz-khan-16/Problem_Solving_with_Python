# 15. [XOR Operation in an Array](https://leetcode.com/problems/xor-operation-in-an-array/)


#         You are given an integer n and an integer start.
#         Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
#         Return the bitwise XOR of all elements of nums.
#         Example 1:
#                   Input: n = 5, start = 0
#                   [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
#                   Output: 8


n=5 
start = 0
o=0
for  i in range(0,n):
    x=start + 2 * i
    o=o^x
    
    
print(o)    




