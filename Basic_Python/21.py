#Fibonacci Series

# 0,1,1,2,3,5,8
# fibo(n)= fibo(n-1)+ fibo(n-2)
x=int(input('number of fibonakki number  '))

def fibo(n):
    if n==0:
       return 0
    if n==1:     
       return 1 
    else:
        return  fibo(n-1)+fibo(n-2) 

for n in range (x):
     print(fibo(n))

