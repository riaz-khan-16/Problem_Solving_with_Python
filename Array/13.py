#leetcode:832. Flipping an Image


image = [[1,1,0],[1,0,1],[0,0,0]]




def flip(array):
    f=[]
    for i in range(len(array)-1,-1,-1):
        f.append(array[i])
    return f       


 
def invert(array):
    i=[]
    for j in array:
        if j==0:
          i.append(1)
        else:  
          i.append(0)  
    return i

final=[]
for i in image:
    i=flip(i)
    i=invert(i)
    final.append(i)  
print(final)
