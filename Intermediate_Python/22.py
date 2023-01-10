# A perfect number is a positive integer that is equal to the sum of its proper positive divisors


a=int(input('take the number: '))
x=0
for i in range(1,a,1):
    if a%i==0:
        x=x+i
print(x)        
if x==a:
    print('Perfect unmber')   
else:
    print('Not')  
