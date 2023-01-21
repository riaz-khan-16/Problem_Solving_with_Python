
matrix=[1,2,3,4,5,6,7,8,9]
n=3
r=n
c=n  
d=[]
m=0
for i in range(0,n):
    b=[]
    for j in range(m,m+c):
        b.append(matrix[j])
    d.append(b)
    m=m+c 
print(d)