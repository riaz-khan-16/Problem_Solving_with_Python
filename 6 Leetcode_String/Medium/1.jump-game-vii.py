#problem Link:   [Jump Game VII](https://leetcode.com/problems/jump-game-vii/)

#Take help from Youtube:

#Solution:


s = "01101110"

minJump = 2
maxJump = 3

def find(s,minJump,maxJump):
    i=0
    j=1
    while i<len(s):
       if s[i]=='0' and i + minJump <= j <= min(i + maxJump, len(s) - 1) and s[j] == '0':
           if j==len(s)-1:
               return True
           i=j  
       j=j+1    
          
    return   False                          
                                                                   
find(s,minJump,maxJump)



def canReach(s, minJump, maxJump):
        if s[-1] == '1': return False
        if minJump <= len(s)-1 <= maxJump: return True
        
        dp = [1]*minJump
        
        for i in range(minJump, len(s)):
            reachable = 0
            if s[i] == '0':
                reachable = dp[i-minJump] - (dp[i-maxJump-1] if i-maxJump > 0 else 0)
            if reachable > 0:
                dp.append(dp[-1] + 1)
            else:
                dp.append(dp[-1])
                
        return reachable>0




