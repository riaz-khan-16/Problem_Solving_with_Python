# 14. [Product of two numbers using Recursion]
#(https://www.geeksforgeeks.org/product-2-numbers-using-recursion/) GFG


x=5
y=9
def p(x,y):

    if y!=0:
        return x+p(x,y-1)
    if y==0:
        return 0

print(p(x,y))    
