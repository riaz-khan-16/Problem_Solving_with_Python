#27. Define two methods to print the maximum and the minimum number
#    among three numbers entered by the user.


a=int(input("Give the 1st number: "))   
b=int(input("Give the 2nd number: "))   
c=int(input("Give the 3rd number: ")) 


def findMax(a,b,c):
     if a>b and a>c :
         print(str(a)+" is maximum value")
     elif b>a and b>c:
         print(str(b)+" is maximum value")
     elif c>a and c>b:
         print(str(c)+" is maximum value")     

def findMin(a,b,c):
     if a<b and a<c :
         print(str(a)+" is minimum value")
     elif b<a and b<c:
         print(str(b)+" is minimum  value")
     elif c<a and c<b:
         print(str(c)+" is minimum  value")  



findMax(a,b,c)
findMin(a,b,c)

