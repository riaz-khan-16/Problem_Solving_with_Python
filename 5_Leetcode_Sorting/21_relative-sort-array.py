#https://leetcode.com/problems/relative-sort-array/

# Given two arrays arr1 and arr2, the elements of arr2 are distinct, 
# and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
# Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

# Example 1:

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
arr1.sort()
def d(arr1,arr2):
    x=[]
    for i in range(len(arr2)):
        for j in (arr1):
            if j==arr2[i]:
                x.append(j)
    for j in range(len(arr1)):  
        if arr1[j] not in arr2:
            x.append(arr1[j])         
    return x            

print(d(arr1,arr2))        


              
      

