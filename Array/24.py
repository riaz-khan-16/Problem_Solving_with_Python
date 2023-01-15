#  Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# A subarray is a contiguous part of array. An array that is inside another array. 
# For example, consider the array [1, 2, 3, 4], There are 10 non-empty sub-arrays.
#  The subarrays are (1), (2), (3), (4), (1,2), (2,3), (3,4), (1,2,3), (2,3,4) and (1,2,3,4). 
#  In general, for an array/string of size n, there are n*(n+1)/2 non-empty subarrays/substrings.

num = [1,2,3,4]

#How to find all sub array of an array

# def sub_arrays(arr):
#     sub_arrays_list = []
#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             sub_arrays_list.append(arr[i:j+1])
#     return sub_arrays_list
# print(len(sub_arrays(num)))

for i in range(len(num)):
        print('value od i:',i)
        for j in range(i, len(num)):
            print('value od j:',j)
            print((num[i:j+1]))





