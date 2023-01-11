# Richest Customer Wealth ( leetcode:1672 )



# accounts = [[1,5],[7,3],[3,5]]
# Output: 10


# Explanation: 
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.



a=[[1,5,6],[7,3,8],[3,5,0]]
r=len(a)
c=len(a[0])
 
m=0 

for i in range(r):  
        x=0      
        for j in range(c):
                x=x+a[j][i]
        if x>m:
          m=x
print(m)        
                  
       


 
 


  
    
   