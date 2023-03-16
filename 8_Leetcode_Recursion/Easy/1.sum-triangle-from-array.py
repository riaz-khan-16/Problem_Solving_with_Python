#1. [Sum Triangle from Array](https://www.geeksforgeeks.org/sum-triangle-from-array/) GFG


#using for loop and while loop

# p=[1,2,3,4,5]

# while len(p)>1:
#         x=[]
#         for i in range(1,len(p)):
#            x.append(p[i-1]+p[i])
           
#         p=x
#         print(p) 
      
# print(p)        


#using Recursion


def printTriangle(A):
           
        # Base case
        if (len(A) < 1):
            return
   
        # Creating new array which contains the
        # Sum of consecutive elements in
        # the array passes as parameter.
        temp = [0] * (len(A) - 1)
        for i in range( 0, len(A) - 1):
           
            x = A[i] + A[i + 1]
            temp[i] = x
           
   
        # Make a recursive call and pass
        # the newly created array
        printTriangle(temp)
           
        # Print current array in the end so
        # that smaller arrays are printed first
        print(A)
       
   
# Driver function
A = [ 1, 2, 3, 4, 5 ]
printTriangle(A)
   