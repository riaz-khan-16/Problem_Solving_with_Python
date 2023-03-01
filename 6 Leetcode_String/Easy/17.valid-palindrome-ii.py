#  https://leetcode.com/problems/valid-palindrome-ii/


#680. Valid Palindrome II





s='abcdefghgfedcxba'

        
# two pointer approach
def isPalindrome(s):
        return s == s[::-1]

def validPalindrome(s):
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                delete_i = s[i+1:j+1]
                delete_j = s[i:j]
                return isPalindrome(delete_i) or isPalindrome(delete_j)
            i += 1
            j -= 1
        return True
    









   


