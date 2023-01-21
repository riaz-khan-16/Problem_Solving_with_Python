#Write a program to print the factorial of a number by defining a method named 'Factorial'
#    Also,
#     1! = 1
#     0! = 1

def factorial(i):
    if i==1 or i==0:
        return 1
   
    x=i
    for n in range(1,i-1):
            x=x*(i-n)
    return x        



a=int(input("Give number: "))    
print(factorial(a))     
          