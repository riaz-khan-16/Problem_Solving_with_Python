# Define a method to find out if a number is prime or not

# method 1
def primeOrNot(x):
        p=[2,3,5,7]
        if x in p:
            return True
        else:
            for i in p:
              if x%i!=0:
                return True
              else:  
                return False

i=int(input("Give the number: "))    
if primeOrNot(i):
    print("Prime")  
else:
    print("Not Prime") 


# method 2:


# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True

# num = 19
# if is_prime(num):
#     print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")

