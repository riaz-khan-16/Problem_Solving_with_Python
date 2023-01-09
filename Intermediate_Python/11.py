#Compound Interest python Program

#A = P(1 + r/n)^(nt)

# Where:

# A is the future value of the investment
# P is the principal amount
# r is the annual interest rate
# n is the number of times the interest is compounded per year
# t is the number of years the money is invested



P=int(input("the principal amount: "))
r=float(input("the annual interest rate: "))
n=int(input("the number of times the interest is compounded per year: "))
t=int(input("the number of years the money is invested: "))


A=P*(1 + r/n)**(n*t)

print(A)