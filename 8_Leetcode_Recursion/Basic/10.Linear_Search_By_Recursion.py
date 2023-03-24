arr=[1,2,3,4,5,9,5,7,8]

target=5


def Find(arr,target,i):

    if arr[i]==target:
        return i
    else:
        return  Find(arr,target,i+1)
    
print(Find(arr,target,0))    