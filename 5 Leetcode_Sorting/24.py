arr =[1024,512,256,128,64,32,16,8,4,2,1]




def find(arr):
        def tobinary(x):
            x=bin(x).replace("0b", "")
            x=str(x) 
            return x.count('1')

        for i in range(len(arr)):
            for j in range(0,len(arr)-1):
               if tobinary(arr[j])>tobinary(arr[j+1]):
                    temp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp
            #    elif tobinary(arr[j+1])==tobinary(arr[j]):
            #         arr[j+1]=max(arr[j+1],arr[j])   
            #         arr[j]=min(arr[j+1],arr[j]) 
            

        return arr        


print(find(arr))
print(bin(8).replace("0b", ""))    