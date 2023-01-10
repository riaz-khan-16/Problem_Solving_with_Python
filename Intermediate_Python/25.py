#25. Kunal is allowed to go out with his friends only on the even days of a 
# given month. Write a program to count the number of days he can go out in the month of August.

m=int(input("Month Name: "))
 
m31=[1,3,5,7,8,10,12]
m28=[2]
if m in m31:
    a=31
elif m in m28:
    a=28
else:
    a=30        

#find even number in 0 to 31
count=0
for i in range(a):
        if i%2==0:
            count=count+1


print("The number of even days in the month is: "+str(count))         


