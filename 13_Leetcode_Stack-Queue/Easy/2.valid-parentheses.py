# 2. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) leetcode

# without stack

s = "()[]{}"

def find(s):
    while '()' in s or '[]' in s or '{}' in s:
            s=s.replace('()','').replace('[]','').replace('{}','')
            if len(s)==0:
                print(True)
            else:
                print(False)

#with stack
#For each character:
#If it's an opening bracket ('(', '{', or '['), push it onto the stack.
#If it's a closing bracket (')', '}', or ']'), check if the stack is empty. If it is, return False because there's no corresponding opening bracket.
#If the stack is not empty, pop the top element from the stack and check if it matches the current closing bracket. If they don't match, return False.
#https://www.youtube.com/watch?v=WTzjTskDFMg&t=363s


stack=[]
s ="()"
close_to_open={"}":"{",")":"(","]":"["}
for i in s:
    if i in close_to_open:
         if stack and stack[-1]==close_to_open[i]:
              stack.pop()
         else:
              print(False)  
    else:
         stack.append(i)   
if not stack:
     print(True)
else:
     print(False)                        
                    


    

