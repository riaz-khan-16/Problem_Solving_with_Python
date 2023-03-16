#[Maximum and Minimum value in an array](https://www.geeksforgeeks.org/recursive-programs-to-find-minimum-and-maximum-elements-of-array/) GFG


a=[2,65,6,8,9,3,5,6,1]

def findMinRec(a, n):
    
    if (n == 1):
        return a[0]
    return min(a[n - 1], findMinRec(a, n - 1))
 

n = len(a)
print(findMinRec(a, n))
 
# This code is contributed by
# Shashank_Sharma