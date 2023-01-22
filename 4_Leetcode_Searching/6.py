#[Arranging Coins(Easy)](https://leetcode.com/problems/arranging-coins/)


# You have n coins and you want to build a staircase with these coins. The staircase consists of k 
# rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

n=10
# 1
# 11
# 111
# 1111

def findK(n):
    x=0
    k=n
    for i in range(n):
        k=k-i
        x=x+i
        while k<x:
            return k
    
print(findK(n))