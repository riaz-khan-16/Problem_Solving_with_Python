#https://leetcode.com/problems/minimum-absolute-difference/


# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr
 

# Example 1:

# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
# Example 2:

# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# Example 3:

# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
arr= [40,11,26,27,-20]


#algorithm:
  # 1.find the minimum difference of a pair
        # i) sort the array
        # ii) check every difference of previos and post
        # iii) find minimum

  # 2. make all possible pairs having the required difference


# 1.find the minimum difference of a pair
        

arr = [4,2,1,3]
arr.sort()
print(arr)

prev=arr[0]
m=float('inf')

for i in range(1,len(arr)):
    diff=abs(arr[i]-prev)
    prev=arr[i]
    if diff<m:
        m=diff 
 

# 2. make all possible pairs having the required difference



pre=arr[0]
x=[]
for i in range(1,len(arr)):
       diff=abs(pre-arr[i])
       if diff==m:
          x.append([pre,arr[i]])
       pre=arr[i] 

print(x)





    



