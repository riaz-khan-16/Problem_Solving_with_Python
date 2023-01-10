#26. Write a program to print the sum of negative numbers, 
# sum of positive even numbers and the sum of positive odd 
# numbers from a list of numbers (N) entered by the user.
#  The list terminates when the user enters a zero.

pe=0
po=0 
n=0
while True:
 i=int(input("Give the input: "))
 if i>0:
   if i%2==0:
        pe=pe+i
   else:
        po=po+i     
 elif i<0:
        n=n+i
 elif i==0:
        break   


print(pe)
print(po)
print(n)


