#leetcode: 1295. Find Numbers with Even Number of Digits

# Given an array nums of integers, return how many of them contain an even number of digits.
# Input: nums = [12,345,2,6,7896]
# Output: 2

num = [12,345,2,6,7896]

def checkEven(a):
    a=len(str(a))
    c=0
    if a%2==0:
       return True  

e=0
for i in num:
    if checkEven(i):
         e=e+1

print(e)