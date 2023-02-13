#20. [Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)


arr =[0,1,2,3,4,5,6,7,8]



def bin1(arr):
    arrb=[]
    for x in arr:
        x=bin(x).replace("0b", "")
        arrb.append(x)
    return arrb


def find(arr):
        def tob(x):
            x=bin(x).replace("0b", "")
            x=str(x) 
            return x.count('1')

        for i in range(len(arr)):
            for j in range(0,len(arr)-1):
               if arr[j]>arr[j+1] and tob(arr[j])==tob(arr[j+1]):
                    temp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp
               elif  tob(arr[j])>tob(arr[j+1]):
                    temp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp
                           
                    
            

        return arr        


print(bin1(arr)) 
print(find(arr))  