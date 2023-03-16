#1. [Sum Triangle from Array](https://www.geeksforgeeks.org/sum-triangle-from-array/) GFG


#using for loop and while loop

p=[1,2,3,4,5]

while len(p)>1:
        x=[]
        for i in range(1,len(p)):
           x.append(p[i-1]+p[i])
           
        p=x
        print(p) 
      
print(p)        