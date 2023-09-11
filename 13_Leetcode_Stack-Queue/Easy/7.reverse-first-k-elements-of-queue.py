# 7. [Reverse First K elements of Queue](https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1/) GFG
l=5
x=3
arr=[1,2,3,4,5]

l=4
x=4
arr=[4,3,2,1]

# first element is arr[x-1]
# 2nd element is arr[x-2]
# xth element is arr[x-x]
# the next is [x]
# the next is [x+1]
# the  lth is [l-1]


ans=[]

for i in range(x):
    ans.append(arr[x-1-i])
for i in range(x,l):
    ans.append(arr[i])
print(ans)    
