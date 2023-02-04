# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
# def selectionSort(array, size):
#     for ind in range(size):
#         min_index = ind
 
#         for j in range(ind + 1, size):
#             # select the minimum element in every iteration
#             if array[j] < array[min_index]:
#                 min_index = j
#          # swapping the elements to sort the array
#         (array[ind], array[min_index]) = (array[min_index], array[ind])
 
# arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
# size = len(arr)
# selectionSort(arr, size)
# print('The array after sorting in Ascending Order by selection sort is:')
# print(arr)


arr=[2,5,9,3,4,1]



def selectionSort(arr):
       size=len(arr)
       for i in range(size):
           min=i
           for j in range(min+1,size):
              if arr[j]<arr[min]:
                min=j
           (arr[i],arr[min])=(arr[min],arr[i])   
       return arr

       
print(selectionSort(arr))            

              
           