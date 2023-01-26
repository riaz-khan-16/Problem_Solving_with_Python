
#Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist/)
# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 

# Example 1:

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

arr = [1,2,5,3]
arr=[-2,0,10,-19,4,6,-8]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]==2*arr[j] and i!=j:
            print(True)
print(False)