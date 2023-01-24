# Kth Missing Positive Number]
# (https://leetcode.com/problems/kth-missing-positive-number/


# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.

 

# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...].
#  The 5th missing positive integer is 9.
arr = [2,3,4,7,11]
k = 5
a=len(arr)
b=[]
for i in range(1,a+k+1):
        if i not in arr:
            b.append(i)
            
print(b[k-1])     
