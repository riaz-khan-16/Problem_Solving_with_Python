#LCM Of Two Numbers

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

for i1 in f1:
    if i1 not in f2:
        f2.append(i1)
    
print(f2)     
       

       
           