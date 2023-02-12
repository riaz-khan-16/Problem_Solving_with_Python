#[Rank Transform of an Array]
# (https://leetcode.com/problems/rank-transform-of-an-array/)

# Example 1:
# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]


# Example 2:
# Input: arr = [100,100,100]
# Output: [1,1,1]



# Example 3:
# Input: c
# Output: [5,3,4,2,8,6,7,1,3]
arr=[2,-11,24,15,26,-31,-48,-49,22,37,-36]


def arrayRankTransform(self, arr):
        # keep unique elements of array in ascending order
    a=list(sorted(set(arr)))
    p={}
    for i,j in enumerate(a):
        p[j]=i+1                        
    return [p[x] for x in arr]

arr1=sorted(set(arr))

x=[]
for i in range(len(arr)):
    for j in range(len(arr1)):
        if arr[i]==arr1[j]:
            arr[i]=j+1
            x.append(j)
print(x)






