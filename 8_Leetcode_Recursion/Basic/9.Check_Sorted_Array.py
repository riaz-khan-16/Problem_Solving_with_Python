arr=[1,2,3,8,12,1]

#Method 1

def check(arr,i):
  
  if i==len(arr)-1:
    return True

  return arr[i]<arr[i+1] and check(arr,i+1)   



#Method 2
def check1(arr,i):
  if i==len(arr)-1:
    return True
  
  elif arr[i]<arr[i+1]:
     return check1(arr,i+1) 
  else:
    return False
  


print(check1(arr,0))



