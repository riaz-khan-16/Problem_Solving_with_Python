# Reverse A String 

# range(stop)
# range(start, stop)
# range(start, stop, step)

x=input("Take the string: ")
y=[]
for n in range(len(x)):
      m=x[n]
      y.append(m)

print(y)      
r=[]
for x in range(len(y),0,-1):
    r.append(y[x-1])

print(r)   

p=r[0]
for n in range(1,len(r),1):
        p=p+r[n]
print(p)
    
