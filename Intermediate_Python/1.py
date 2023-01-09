# 1. Factorial Program
# formula: n=n*(n-1)*(n-2)....

x=int(input('Give the number: '))

fact=1

for n in range(x):
    print("x: "+ str(x))
    print("n: "+ str(n))
    z=x-n
    print("z=x-n=: "+ str(z))
    fact=fact*z
      
print(fact)         


      
     