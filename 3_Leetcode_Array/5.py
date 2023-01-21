#Shuffle the Array leetcode 1470

# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
nums = [1,2,3,4,4,3,2,1]
n=4
a=[]
for i in range(n):
    a.append(nums[i])


b=[]
for j in range(n,2*n,1):
    b.append(nums[j])



x=[]

for k in range(n):
    x.append(a[k])
    x.append(b[k])
print(x)

