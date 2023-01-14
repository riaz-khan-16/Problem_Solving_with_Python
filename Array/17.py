
#leetcode: 867. Transpose Matrix


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]

matrix = [[1,2,3],[4,5,6],[7,8,9]]


matrix1=[]
for i in range(len(matrix[0])):
    matrix2=[]
    for j in range(len(matrix)):
        matrix2.append(matrix[j][i])
    matrix1.append(matrix2)    

print(matrix1)


