#Leetcode:1886. Determine Whether Matrix Can Be Obtained By Rotation
#https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation

mat =[[0,0,0],[0,0,1],[0,0,1]]
target =[[0,0,0],[0,0,1],[0,0,1]]
#make a method for find tranpose of a matrix

def findtranpose(a):
        t=[]
        for i in range(len(a)):
            to=[]
            for j in range(len(a[0])):
                to.append(a[j][i])
            t.append(to)     
        return t




#make a method to rever a row element :
def reverseRow(a):
        rr=[]
        b=len(a)
        for i in range(len(a)):
            rr.append(a[b-i-1])
        return rr





#make a method to rever all row element:
def reverseAllRow(a):
        rra=[]
        for i in a:
            rra.append(reverseRow(i))
        return rra    






# make a method to find if two matrix is equal or not
def isTwoMtrixEqual(mat1,mat2):
        if mat1==mat2:
            return True
        else:    
            return False    

# make a method to rotate 90 degree once
def rotate90(mat):
    mat=findtranpose(mat)    
    mat=reverseAllRow(mat)
    return mat
# mat=rotate90(mat)
# mat=rotate90(mat)
# result=isTwoMtrixEqual(mat,target)
# print(result)    
r=0
for i in range(4):
        mat=rotate90(mat)  
        result=isTwoMtrixEqual(mat,target)
        if result:
                r=1
             
if r==1:
    print(True)
else:    
    print(False)