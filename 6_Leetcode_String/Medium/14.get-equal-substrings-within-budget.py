#problem Link:   14. [Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/)


#Take help from Youtube:

#Solution:


def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        cost=0
        l=0
        ans=0
        for r in range(len(s)):
            
            cost+= abs(ord(s[r])-ord(t[r]))
            while cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l+=1
            ans=max(ans,  r-l+1)
        return ans
            