# Take integer inputs till the user enters 0 and print the largest number from all.



n=0

while True:
     x=int(input('Take Input( 0 for quit): '))
     if x==0:
        break
     if x>n:
        n=x

print(n)     
