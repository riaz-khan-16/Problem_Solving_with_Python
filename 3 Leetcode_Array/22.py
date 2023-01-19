# 22. Find N Unique Integers Sum up to Zero
# (https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

n=4
#if odd:

if n%2==1:
    n1=-int((n-1)/2)
    n2=int((n-1)/2)+1
    a=0
    b=[]
    for i in range(n1,n2,1):
        a=a+i
        b.append(i)
    print(b)    
#if even:   
else:
    n=int(n/2)
    b=[]
    for i in range(1,n+1):
        ng=-i
        np=i
        print(ng,np)
        b.append(ng)
        b.append(np)
    print(b)    