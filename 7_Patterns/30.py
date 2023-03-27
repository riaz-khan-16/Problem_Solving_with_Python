    #         1
    #       2 1 2
    #     3 2 1 2 3
    #   4 3 2 1 2 3 4
    # 5 4 3 2 1 2 3 4 5



  
n=5

for i in range(0,n):

    for k in range(n-1,i,-1):
           print('  ',end='')


    for j in range(i+1,0,-1):
           print(j,end=' ')

    for j in range(1,i+1):
           print(j+1,end=' ')       

    print('')       

    

