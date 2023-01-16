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


#go left to right

for i in range(left,right): #row fixed

     a.append(matrix[top][i])

right=right-1
#go top to bottom
for i in range(top,bottom): #column fixed
    a.append(matrix[i][right])
bottom=bottom-1
# left to right

for i in range(right,left,-1):
    a.append(matrix[bottom][i])

left=left-1
print(a)  



