# 11. [Recursive Bubble Sort](https://www.geeksforgeeks.org/recursive-bubble-sort/) GFG


arr=[3,2,1,0,5]

def f(arr,r,c):

    if r==0:
        return
    if r>c:
        if arr[c]>arr[c+1]:
            arr[c],arr[c+1]=arr[c+1],arr[c]
        f(arr,r,c+1)

    else:
        f(arr,r-1,0)

f(arr,4,0)    
print(arr)    
