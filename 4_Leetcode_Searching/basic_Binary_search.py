# def binarySearch(array, x, low, high):

#     # Repeat until the pointers low and high meet each other
#     while low <= high:

#         mid = low + (high - low)//2

#         if array[mid] == x:
#             return mid

#         elif array[mid] < x:
#             low = mid + 1

#         else:
#             high = mid - 1

#     return -1


# array = [3, 4, 5, 6, 7, 8, 9]
# x = 5
# result = binarySearch(array, x, 0, len(array)-1)

# if result != -1:
#     print("Element is present at index " + str(result))


array=[1,2,3,4,5]



def binarySearch(target,array):
        start=0
        end=len(array)-1
        while start<=end:
            mid=int((start+end)/2)
            if array[mid]==target:
                return mid
            elif array[mid]>target: #go left
                end=mid-1
            else:# go right
                start=mid+1
        return -1        

print(binarySearch(6,array))
