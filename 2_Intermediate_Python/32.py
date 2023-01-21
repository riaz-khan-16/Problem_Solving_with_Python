# 32.Write a program to print the circumference and area of a circle of radius entered by user by
#  defining your own method


r=int(input("Give the radius: "))   

def curcumference(r):
       print(2*3.14*r)

def area(r):
       print(3.14*r**2)

curcumference(r)

area(r)
