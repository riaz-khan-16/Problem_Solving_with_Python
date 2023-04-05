

def f(arr):

    if len(arr)==1:
        return True 

    if arr[0]>arr[1]:
        return False
    
    return f(arr[1:])

print(f([1,2,5,6,7,8,3]))    