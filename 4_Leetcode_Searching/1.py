# 1. Square Root(https://leetcode.com/problems/sqrtx/)

x=18
start=1
end=x

def findsquare(x,start,end):
    while start+1<end:
        mid=(start+end)//2
        
        if mid*mid>x:   
            end=mid
        if mid*mid<x:
            start=mid
        if mid*mid==x:
            return mid
    if start*start==x:
        return start     
    return int((start+end)/2)  
    
print(findsquare(x,start,end))     

#first iteration: start=1, end=18, mid=9,mid*mid=81>18    start+1=2<end=18
#2nd iteration: start=1, end=9, mid=5,mid*mid=25>18        start+1=2<end=9
#3rd iteration: start=1, end=5, mid=3,mid*mid=9<18          start+1=2<end=5
#4th  iteration: start=3, end=5, mid=4,mid*mid=16<18         start+1=4>end=5
#5th iteration: start=4, end=5, mid=4,mid*mid=16<18          start+1=5>end=5   loop broken

# return int(4+5)/2


#
