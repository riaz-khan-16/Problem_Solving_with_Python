#59. Spiral Matrix 
# https://leetcode.com/problems/spiral-matrix


matrix =[[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]
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

        if not (top<bottom and left<right):
            break  

        # # right to left:(row=bottom)
        for k in range(right-1,left-1,-1):
            a.append(matrix[bottom-1][k])
        bottom=bottom-1


        #bottom to top:(column:left)
        for h in range(bottom-1,top-1,-1):
            a.append(matrix[h][left])
        left=left+1


            


                 

print(a)  

# code for reshapeing
# r=len(matrix)
# c=len(matrix[0])

# d=[]
# m=0
# for i in range(0,r):
#     b=[]
#     for j in range(m,m+c):
#          b.append(a[j])
#     d.append(b)
#     m=m+c 
      
# print(d)