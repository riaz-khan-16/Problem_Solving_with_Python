#59. Spiral Matrix 
# https://leetcode.com/problems/spiral-matrix

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
a=[]
left=0
right=len(matrix[0])
top=0
bottom=len(matrix)

while top<bottom and left<right:
            #left to right:(row=top)
            for i in range(left,right):
                a.append(matrix[top][i])
            top=top+1
            # top to bottom:(column=right)

            for j in range(top,bottom):
                a.append(matrix[j][right-1])
            right=right-1

            # right to left:(row=bottom)
            for k in range(right,left,-1):
                a.append(matrix[bottom-1][k-1])

            bottom=bottom-1
            #bottom to top:(column:left)
            for h in range(bottom,top,-1):
                a.append(matrix[top][left])
            left=left+1

print(a)  

c=[]
n=3
m=0
for i in range(n):
    b=[]
    for j in range(m,m+3):
         b.append(a[j])
    c.append(b)
    m=m+3    
print(c)