
# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

a=[1,2,3,4,5,5,5]
x=0
for i in range(1,len(a)):
    if a[i]!=a[x]:
        x=x+1
        a[x]=a[i]
print(x+1)