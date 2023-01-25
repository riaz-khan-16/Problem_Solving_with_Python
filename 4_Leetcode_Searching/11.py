# 11. [Count Negative Numbers in a Sorted Matrix]
# (https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)


# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and
#  column-wise, return the number of negative numbers in grid.

 

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
grid = [[3,2],[1,0]]
arr=[-1,-1,-2,-3]
def findNegative(arr):
       start=0
       end=len(arr)
       while start+1<end:
            mid=(start+end)//2
            if arr[mid]<0 and arr[mid-1]>0:
                return mid
            elif arr[mid]>=0:
                 start=mid
            else:
                end=mid
       return  start       
print(findNegative(arr))


neg=0
for i in grid:
       neg=neg+(len(i)-findNegative(i))
print(neg)
