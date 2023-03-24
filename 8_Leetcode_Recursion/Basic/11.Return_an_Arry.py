arr=[1,2,3,4,4,5,6]
target=4

l=[]


def F(arr,target,index,l):
         end=len(arr)-1
         if index==end:
                 return l
         if arr[index]==target:
                l.append(index)
                return F(arr,target,index+1,l) 

         else:
            return F(arr,target,index+1,l)        
             


print(F(arr,target,0,l))
