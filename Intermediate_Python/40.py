#Write a function that returns the sum of first n natural numbers


def sumOfNaturalNumber(n):
            t=0
            for i in range(0,n+1,1):
                t=t+i
            return t        


n=2
print(sumOfNaturalNumber(n))           