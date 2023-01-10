# Write a function that returns all prime numbers between two given numbers

def findinrange(a,b): 
    def is_prime(n):
        if n<=1:
            return False
        for i in range(2,n):
            if n%i == 0:
                return False
        return True
                
    p=[] 

    for j in range(a+1,b-1,1):
      if is_prime(j):
          p.append(j)         
    print(p)            



a=int(input("a: "))
b=int(input("b: "))
findinrange(a,b)