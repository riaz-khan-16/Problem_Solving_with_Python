
# Stack has two method:
#                  1. Push
#                  2. Pop



# Implement Stack Using List


def push(arr,x):
    arr=list(arr)
    arr.append(x)
    return arr
def pop(arr):
    arr=list(arr)
    arr.pop(len(arr)-1)
    return arr
arr=[]
arr=push(arr,5)
print(arr) 
  
arr=pop(arr) 
print(arr)








