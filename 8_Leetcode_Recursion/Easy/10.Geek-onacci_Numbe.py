# 10. [Geek-onacci Number](https://practice.geeksforgeeks.org/problems/geek-onacci-number/0/) GFG
A = 1
B = 3
C = 2
N = 4


def Fi(x):
    if x==1:
        return 1
    if x==2:
        return 3
    if x==3:
        return 2 
    return Fi(x-1)+Fi(x-2)+Fi(x-3)
   
print(Fi(6))  