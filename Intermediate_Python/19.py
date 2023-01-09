#HCF Of Two Numbers 

x=int(input("Take first number: "))
f1=[x]
for n in range (2,x,1):
    if x%n==0:
        f1.append(n)
  


y=int(input("Take 2nd number: "))
f2=[y]
for n in range (2,y,1):
    if y%n==0:
        f2.append(n)


hcf=[]
for i1 in f1:
    for i2 in f2:
        if i1==i2:
            hcf.append(i2)
print(hcf) 
       
           