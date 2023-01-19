#Leetcode: 1252. Cells with Odd Values in a Matrix



m = 1
n = 1
indices = [[0,0],[0,0]]
         
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
                matrix[r][i]=matrix[r][i]+1
        return matrix

def columIncrement(c,matrix):
        for i in range(len(matrix)):
                matrix[i][c]=matrix[i][c]+1
        return matrix

def findRC(indices):      
        r=[]
        c=[]
        for a,b in indices:
                r.append(a)
                c.append(b)
        return r,c 
        
r,c=findRC(indices)

def finalIncrement(r,c,matrix):
                for i in r:
                    matrix=rowIncrement(i,matrix)
                for j in c:
                    matrix=columIncrement(j,matrix)
                return matrix

matrix=finalIncrement(r,c,matrix)

def calculateoddNumber(matrix):
        o=0
        for i in matrix:
                for j in i:
                        
                        if j%2!=0:
                                o=o+1
        return o                


odd=calculateoddNumber(matrix)

print(odd)