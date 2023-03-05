# [Count Items Matching a rule](https://leetcode.com/problems/count-items-matching-a-rule/)



# 1773. Count Items Matching a Rule


def countMatches(self, items, ruleKey, ruleValue):
            if ruleKey=="color":
                 i=1
            elif ruleKey=="type":
                  i=0
            else:
                  i=2  
            a=0
            for j in range(len(items)):
                if items[j][i]==ruleValue: 
                   a=a+1 
            return a