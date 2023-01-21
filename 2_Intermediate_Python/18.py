# Factor a number


x=20
f=[x]
for n in range (2,x,1):
    if x%n==0:
        f.append(n)
print(f)        


