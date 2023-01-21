#73. Set Matrix Zeroes
#https://leetcode.com/problems/set-matrix-zeroes/

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
a=[]
for i in range(len(matrix)):
       for j in range(len(matrix[0])):
             if  matrix[i][j]==0:
                a.append([i,j])


for i,j in(a):  
        for x in range(len(matrix[0])):
                matrix[i][x]=0
        for x in range(len(matrix)):
                matrix[x][j]=0
print(matrix)   


         