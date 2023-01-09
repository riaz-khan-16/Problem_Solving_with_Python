#Find if a number is palindrome or not


x=input("Take the number: ")
y=[]
for n in range(len(x)):
      m=x[n]
      y.append(m)
     
r=[]
for l in range(len(y),0,-1):
    r.append(y[l-1])

 

p=r[0]
for n in range(1,len(r),1):
        p=p+r[n]

x=int(x)
p=int(p)
if x==p:
     print("palindrome")
else:
    print("not palindrome")