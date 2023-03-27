    #      1
    #     212
    #    32123
    #   4321234
    #    32123
    #     212
    #      1


n=4
for i in range(2*n):
   
   if i<n:
       x=i
   else:
       x=2*n-i  

   if i<n:
       y=n-i
   else:
       y=i-n    

 

   for j in range(0,y+1):
       print(' ',end='') 
   

   for j in range(x,1,-1):
       print(j,end='') 
   for j in range(0,x):
       print(j+1,end='') 
   print('')    

