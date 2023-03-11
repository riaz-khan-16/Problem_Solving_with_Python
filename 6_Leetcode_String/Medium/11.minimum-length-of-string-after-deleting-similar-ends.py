#problem Link:  11. [Minimum Length of String After Deleting Similar Ends](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/)


#Take help from Youtube:

#Solution:

def minimumLength(self, s):
        while len(s) > 1 and s[0] == s[-1]:
            s = s.strip(s[0])
        return len(s)