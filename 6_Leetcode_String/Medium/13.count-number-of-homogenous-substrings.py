#problem Link:  13. [Count Number of Homogenous Substrings](https://leetcode.com/problems/count-number-of-homogenous-substrings/)


#Take help from Youtube:

#Solution:https://leetcode.com/problems/count-number-of-homogenous-substrings/solutions/1064598/python-one-pass-with-explanation/


def countHomogenous(self, s: str) -> int:
        res, count, n = 0, 1, len(s)
        for i in range(1,n):
            if s[i]==s[i-1]:
                count+=1
            else:
                if count>1:
                    res+=(count*(count-1)//2)
                count=1    
        if count>1:
            res+=(count*(count-1)//2)
        return (res+n)%(10**9+7)