#  5. [132 Pattern](https://leetcode.com/problems/132-pattern/) leetcode

#could not do


# brute force

a=[]

#find j

stack=[]

for i in range(len(a)):
    if not stack:
        stack.append([a[i],i])
        
    while stack  and stack[-1][0]< a[i]:
        stack.pop()
        continue
    stack.append([a[i],i])

j=stack[0][0]
index_of_j=stack[0][-1]



#find i
min=a[0]
for i in range(1,index_of_j):
    if a[i]<min:
        min=a[i]
i=min

#find k

for x in range(index_of_j,len(a)):
    if j>a[x]>i:
        print(a[x])

















