# ****
# ***
# **
# *

#Print the pattern by recursion


def patt(r,c):

    if r==0:
        return
    
    if r>c:
        print('*',end='')
        patt(r,c+1)
        
    else:
        print('')
        patt(r-1,0)


patt(4,0)      
            

