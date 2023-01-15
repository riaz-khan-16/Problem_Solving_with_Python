# Leetcode: 1380. Lucky Numbers in a Matrix
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

matrix=[[7,8],[1,2]]
a=matrix

#Need to access all element of the matrix and their position index

#make a method to find maximum element of a column j
def findMaxinColJ(a,j):
        b=[]
        for i in range(len(a)):
            b.append(a[i][j])
        return max(b)



#make a method to find maximum element of a row k

def findMinInRowK(a,k):
        minInRo=min(a[k])
        return minInRo


#find index of min value:

def findIndexOfX(a,x):
        for i in range(len(a)):
                if a[i]==x:
                        index=i
        return index
l=[]
for i in range(len(a)):
        
        x=findMinInRowK(a,i)  
         
        j=findIndexOfX(a[i],x)
      
        r=findMaxinColJ(a,j)
        
        if x==r:
                l.append(x)
print(l)        
       


   
               
   

              



