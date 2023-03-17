# 6. [Print 1 To N Without Loop](https://practice.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1/) GFG
#Print numbers from 1 to N without the help of loops.



N=6

def printN(n,N):
    if n>N:
        return
    print(n,end=' ')
    printN(n+1,N)

printN(1,6)