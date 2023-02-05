

arr=[3,2,4,1,5,6,8,7,10,9]


def selectionSort(arr):
    z=len(arr)
    for i in range(1,z):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j=j-1

selectionSort(arr)
print(arr)
