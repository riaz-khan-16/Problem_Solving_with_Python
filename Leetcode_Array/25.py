#566. Reshape the Matrix
#https://leetcode.com/problems/reshape-the-matrix/


mat = [[1,2],[3,4]]
r = 1
c = 4


r1,c1=len(mat),len(mat[0])

if r*c==r1*c1:
       a=[]
       for i in mat:
            for j in i:
                a.append(j)  
       n=0
       d=[]
       for i in range(r):
            b=[]
            b.append(a[n:n+c])
            n=n+c
            d.append(b[0])
       print(d)  
         
            
else:
        print(mat)
          
 




             