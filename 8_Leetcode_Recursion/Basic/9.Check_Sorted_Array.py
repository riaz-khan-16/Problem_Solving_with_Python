arr=[1,2,1,8,12]

def check(arr,i):
  
  if i==len(arr)-1:
    return True

  return arr[i]<arr[i+1] and check(arr,i+1)   

print(check(arr,0))