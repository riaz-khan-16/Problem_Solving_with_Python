#Input a number and print all the factors of that number (use loops)

x=int(input('Take input number: '))
y=[]

for n in range(x):
            n=n+1
            if (x%n)==0:
                y.append(n)
              
print(y) 