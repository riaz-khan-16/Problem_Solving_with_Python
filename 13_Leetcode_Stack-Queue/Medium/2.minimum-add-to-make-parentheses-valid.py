# 2. [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) leetcode
stack=[]
open='('
close=')'
s='((('
if not s:
    print(0)
for i in s:
    if not stack:
        stack.append(i)
    elif stack[-1]==open and  i==close:
        stack.pop()
    else:
        stack.append(i)
    print(stack)   


print(len(stack))       
