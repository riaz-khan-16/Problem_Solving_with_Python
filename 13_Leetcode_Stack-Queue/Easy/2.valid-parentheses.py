# 2. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) leetcode

# without stack

s = "()[]{}]"

def find(s):
    while '()' in s or '[]' in s or '{}' in s:
            s=s.replace('()','').replace('[]','').replace('{}','')
            if len(s)==0:
                print(True)
            else:
                print(False)


#with stack


stack=[]

for i in s:
     if i=='(':
          stack.append()




    

