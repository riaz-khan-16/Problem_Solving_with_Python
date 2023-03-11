#problem Link:   12. [Number of Substrings With Only 1s](https://leetcode.com/problems/number-of-substrings-with-only-1s/)

#Take help from Youtube:

#Solution:
def numSub(self, s):
        res, currsum = 0,0
        for digit in s:
            if digit == '0':
                currsum = 0
            else:
                currsum += 1 
                res+=currsum 
        return res % (10**9+7)