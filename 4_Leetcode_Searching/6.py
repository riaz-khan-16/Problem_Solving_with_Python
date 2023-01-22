#[Arranging Coins(Easy)](https://leetcode.com/problems/arranging-coins/)


# You have n coins and you want to build a staircase with these coins. The staircase consists of k 
# rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

n=5
# 1
# 11
# 111
# 1111
# Linear Search
# def findK(n):
    
#     k=n
#     r=0
#     for i in range(n):
#         k=k-i  
#         while k<=i:
#             return r
#         r=r+1   
    
# print(findK(n))