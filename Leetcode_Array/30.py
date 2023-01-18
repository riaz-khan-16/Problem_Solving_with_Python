#59. Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii/
# Input: n = 3
# Output: [[1,2,3],
#          [8,9,4],
#          [7,6,5]]

# make a zero matrix
def makeZeroMatrix(n):
        a=[]
        for i in range(n):
            b=[]
            for j in range(n):
                b.append(0)
            a.append(b)
        return a

n=5
z=makeZeroMatrix(n)

x=1
top=0
bottom=n
left=0
right=n



while top<bottom and left<right:
        for i in range(left,right): #top row
            z[top][i]=x
            x=x+1
        top=top+1

        for j in range(top,bottom):  #right column
            z[j][right-1]=x
            x=x+1
        right=right-1    


        for k in range(right-1,left-1,-1):   #bottom row
            z[bottom-1][k]=x
            x=x+1
        bottom=bottom-1

        for l in range(bottom-1,top-1,-1):   # left column
            z[l][top-1]=x
            x=x+1   
        left=left+1    

# for m in range(left,right):
#     z[top][m]=x
#     x=x+1
    
         

print(z)














