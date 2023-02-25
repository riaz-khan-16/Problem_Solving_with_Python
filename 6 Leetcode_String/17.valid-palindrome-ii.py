#  https://leetcode.com/problems/valid-palindrome-ii/


#680. Valid Palindrome II


#method 1: Brute Force

# Algo:
#      1. check it palindrome or not
#      If not:
#             2. remove one  character and check 
#             3. do it for n time 


a='abcdefghgfedcxba'

def isPalindrome(a):
    b=a[::-1]
    if a==b:
        return True
    else:
        return False
        









   


