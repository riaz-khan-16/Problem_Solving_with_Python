# [Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin

moves = "LL"
a,b=0,0

for i in moves:
    if i=='R':
        a=a+1
    elif i=='L':
        a=a-1
    elif i=='U':
        b=b+1
    elif i=='D':
        b=b-1
if a==0 and b==0:
    print(True)   
else:
    print(False)        

                    
        