#1. [Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/) leetcode


stack=[]
max=3
def push(x):
    if len(stack)<max:
        stack.append(x)


def pop():
    if not stack:
         return -1
    x=stack[-1]
    stack.pop()
    return x

def inc(k,val):

    if len(stack)<k:
        for i in range(len(stack)):
                stack[i]=stack[i]+val
    else:
        for i in range(0,k):
            stack[i]=stack[i]+val


push(1)  
push(2)
pop()
push(2)  
push(3)
push(4)  
inc(5, 100)
inc(2, 100)
pop()
pop()
pop()



print(stack)

       