#leetcode: 1572. Matrix Diagonal Sum


# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
mat = [[1,2,3,5],
       [4,5,6,5],
       [7,0,9,5],
       [3,8,6,5]]

# mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]

def findshape(matrix):
    x,y=len(mat),len(mat[0])
    return x,y


def findDiagonal1(mat):
    d1=0
    for i in range(x):
        d1=d1+mat[i][i]
    return d1   


def findDiagonal2(mat):
    d2=0
    for i in range(x):
            d2=d2+mat[i][x-1-i]  
            
    return d2

x,y=findshape(mat)
d1=findDiagonal1(mat)
d2=findDiagonal2(mat)

#check any middle element is there or not
if x%2==0:
    c=0
else:
    x=int((x-1)/2)   
    c=mat[x][x] 

     

# find total sum
d=d1+d2-c 

print(d)
