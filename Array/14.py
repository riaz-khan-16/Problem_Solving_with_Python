#Leetcode: 1252. Cells with Odd Values in a Matrix



m = 2
n = 3
indices = [[0,1],[1,1]]
         
#make a method for creating a 0 matrix of m*n dimension
def createMatrix0(m,n):
        matrix=[]
        for i in range(m):
               prematrix=[]
               for j in range(n):
                    prematrix.append(0)
               matrix.append(prematrix)    
        return matrix
matrix=createMatrix0(m,n)  


def rowIncrement(r,matrix):
        for i in range(len(matrix[r])):
                matrix[r][i]=+1
        return matrix

def columIncrement(c,matrix):
        for i in range(len(matrix)):
                matrix[i][c]=matrix[i][c]+1
        return matrix


