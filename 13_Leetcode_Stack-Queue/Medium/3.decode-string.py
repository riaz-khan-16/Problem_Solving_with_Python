# 3. [Decode String](https://leetcode.com/problems/decode-string/) leetcode





s = "3[a2[c]]"

stack=[]
current_num=0
current_str=''

for i in s:
    if i.isdigit():
        current_num=current_num*10+int(i)
    if i=='[':
        stack.append(current_str)    
        stack.append(current_num)
        current_num=0
        current_str=''

    if i==']':
        num=stack.pop()
        prev_str = stack.pop()    
        current_str = prev_str + num * current_str   


    else:
        current_str=current_str+i    