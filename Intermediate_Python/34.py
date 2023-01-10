# 34.Write a program that will ask the user to enter his/her marks (out of 100).
#  Define a method that will display grades:
#80=<x  ----->  A+
#80>x>=70 -----> A
#70>x>=60 ------> A-
  

def grade(m):
    if 80<=m:
        print("A+")
    elif 80>m>=70:
        print("A+")
    elif  70>m>=60:
         print("A-")   
    else:     
         print("F")  


i=int(input("Enter Your Mark: "))     
grade(i)    