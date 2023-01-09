# Subtract the Product and Sum of Digits of an Integer

x=int(input('take input number: '))
x=str(x)
x=list(x)

# at first create an array of the digits
z=[]
for n in range(len(x)):
          y=int(x[n])
          z.append(y) 
      
print(z)   


# find the summation:
y=0
for n in range (len(z)):
            x=z[n]
            y=y+x
print("the sum of the digits is:" + str(y))   

# find the multiplication
y=1
for n in range (len(z)):
            x=z[n]
            y=y*x
print("the multiplication of the digits is:" + str(y)) 