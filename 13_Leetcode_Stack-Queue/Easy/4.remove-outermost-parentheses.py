# 4. [Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/) leetcode


s = "(()())(())"
stack=[]
ans=[]
    

# take a parenthesis
# check weather the stack is not empty and its last element is '(' 
# if yes check the element is ')' or not
# if yes pop it .... if not append it..


for i in s:
   
    if stack:
        if i==')' and stack[-1]=='(':
            stack.pop()
            if stack:
                ans.append(i)
        else:
            stack.append(i)
            ans.append(i)

    else:
        stack.append(i)            
     
print(stack,ans)


         











