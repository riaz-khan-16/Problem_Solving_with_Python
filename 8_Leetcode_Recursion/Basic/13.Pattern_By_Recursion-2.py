# ****
# ***
# **
# *

#Print the pattern by recursion


def patt(r,c):

    if r==0:
        return
    
    if r>c:
        
        patt(r,c+1)
        print('*',end='')
        
    else:
        
        patt(r-1,0)
        print('')

patt(4,0)      
            

