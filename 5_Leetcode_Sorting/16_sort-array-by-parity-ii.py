
# [Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/)

nums = [4,2,5,7]
x=[]
y=[]
for i in range(len(nums)):
    if nums[i]%2==0:
        x.append(nums[i])

for i in range(len(nums)):
    if nums[i]%2==1:
        y.append(nums[i])
z=[0]*len(nums)

print(x)
j=0
for i in range(len(x)):
    z[j],x[i]=x[i],z[j]
    j=j+2
k=1    
for i in range(len(y)):
    z[k],y[i]=y[i],z[k]
    k=k+2    
print(z)    
