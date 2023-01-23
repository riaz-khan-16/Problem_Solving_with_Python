#[Arranging Coins(Easy)](https://leetcode.com/problems/arranging-coins/)


# You have n coins and you want to build a staircase with these coins. The staircase consists of k 
# rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

# n=10
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


# Binary Search 

# formula:
#maximum coin need to make n rows is:
        #                                n(n+1)/2
        #                                for 4 row=20/2= 10 coin
        #                                for 3 row= 6

n=8
def findk(n):
    start=1
    end=n
    
    while start+1<end:
        mid=(start+end)//2
        if mid*(mid+1)/2==n:
            return mid
        elif mid*(mid+1)/2>n:
            end=mid
        else:
            start=mid     
    return start
print(findk(n))




