#Leetcode: 1252. Cells with Odd Values in a Matrix


# #create 0 matrix
# matrix = []
# for i in range(2):
#     row = []
#     for j in range(3):
#         row.append(0)
#     matrix.append(row)

m = 2
n = 3
indices = [[0,1],[1,1]]
         
op=0
arr = [[0]*m for i in range(n)]   #creating the array
for i in indices:
    for j in range(0,m):
            arr[i[0]][j]+=1  
                    #incrementing the row elements
#     for j in range(0,n):
#             arr[j][i[1]]+=1     #incrementing the column elements
# for i in range(0,n):
#     for j in range(0,m):
#         if(arr[i][j]%2!=0):    #finding the odd numbers
#                 op+=1
# print(op)         
      
       


       
    
