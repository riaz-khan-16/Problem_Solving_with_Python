#  Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# A subarray is a contiguous part of array. An array that is inside another array. 
# For example, consider the array [1, 2, 3, 4], There are 10 non-empty sub-arrays.
#  The subarrays are (1), (2), (3), (4), (1,2), (2,3), (3,4), (1,2,3), (2,3,4) and (1,2,3,4). 
#  In general, for an array/string of size n, there are n*(n+1)/2 non-empty subarrays/substrings.

num=[1,2,-3,4,-6,-2]
#method for finding all sub array

def finaAllSubArra(num):
        a=[]
        for i in range(len(num)):
                    for j in range(i,len(num)):
                        a.append(num[i:j+1])
        return a



#method for making sum of a array:
def sumofAnarray(a):
            b=0
            for i in a:
                b=b+i
            return b

def findIndexOfX(a,x):
        for i in range(len(a)):
                if a[i]==x:
                        index=i
        return index




a=finaAllSubArra(num)
b=[]
for i in a:
         b.append(sumofAnarray(i))   
c=max(b)    

print(c)
