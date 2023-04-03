


arr=[3,2,1,0,5]

def f(arr,r,c,max):

    if r==0:
        return
    if r>c:

        if arr[c]>arr[max]:
             f(arr,r,c+1,c)
        else:
            f(arr,r,c+1,max)     
    
    else:
        arr[r-1],arr[max]=arr[max],arr[r-1]
        f(arr,r-1,0,0)

f(arr,4,0,0)    
print(arr)    


