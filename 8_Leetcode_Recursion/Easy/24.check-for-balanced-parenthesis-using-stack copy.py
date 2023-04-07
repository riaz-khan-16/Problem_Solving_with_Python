#  24. [Check for balanced paranthesis using recursion without stack.]
#(https://www.geeksforgeeks.org/check-for-balanced-parenthesis-without-using-stack/) GFG






def closingof(x):

    if x=='[':
        return ']'
    if x=='(':
        return ')'
    if x=='{':
        return '}'
    
exp = '[()]]'

def check(exp):

        unclosed=[]
        open='[({'

        for i in exp:
            if len(unclosed)>=1 and i==closingof(unclosed[-1]):
                unclosed.pop()
                pass
            elif i in open:
                unclosed.append(i)
            else:
                return False    
            
            
        if len(unclosed)==0:
            return True  
        else:
            return False      

print(check(exp))


 