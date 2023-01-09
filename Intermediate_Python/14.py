# Armstrong Number


# An Armstrong number is a number that is the sum of its own digits when each digit is
#  raised to the power of the number of digits

# 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371



x=input("Take the number: ")
z=0
for n in range(len(x)):
    y=int(x[n])
    z=z+y**3
print(z)   
x=int(x) 
if x==z:
    print("The number is an armstrong number")   
else:
    print("The number is not an armstrong number")  
