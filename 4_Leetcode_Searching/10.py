 #[Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)


#  An array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.

 

# Example 1:

# Input: arr = [0,1,0]
# Output: 1



arr =[0,1,2,4,5,5]
start=0
end=len(arr)-1
def findMountain(arr,start,end):
    while start+1<end:
        mid=(start+end)//2
        if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
            return mid
        elif  arr[mid]<=arr[mid+1]: # go right
             start=mid
        else:
            end=mid   
    return end

print(findMountain(arr,start,end))        

