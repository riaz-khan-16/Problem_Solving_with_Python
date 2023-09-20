#1. [Longest Valid Parantheses](https://leetcode.com/problems/longest-valid-parentheses/) 

s=s = "()(()"

left=0
right=0
m=0

for i in range(len(s)):

    
    if s[i]=='(':
        left=left+1
    else:
        right=right+1



    if right==left:
        m=max(m,right*2)

    elif right>left:
        left=0
        right=0  
        
left=0
right=0        
for i in range(len(s)-1,-1,-1):

    
    if s[i]=='(':
        left=left+1
    else:
        right=right+1



    if right==left:
        m=max(m,left*2)

    elif right<left:
        left=0
        right=0  


return m