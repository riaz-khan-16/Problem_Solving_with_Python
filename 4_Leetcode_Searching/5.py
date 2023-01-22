# Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/


# 367. Valid Perfect Square:

# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words,
  # it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.


# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

#Linear Search
# num = 16
# for i in range(num):
#     if i*i==num:
#         print(True)

#Binary Search:

num=1
start=1
end=num
def isSquare(num,start,end):
        
        while start+1<end:
            mid=(start+end)//2
            if mid*mid==num:
                return True
            elif mid*mid>num:
                end=mid
            else:
                start=mid  
        if start*start==num:
            return True         
        return False   

       
print(isSquare(num,start,end))


