# [Fair Candy Swap](https://leetcode.com/problems/fair-candy-swap/)

al = [2,6,9]
bo = [1,3,1]

def sum(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return sum
a=sum(al)
b=sum(bo)   
Sa, Sb = a, b
setB = set(bo)
for x in al:
    if x + (Sb - Sa) / 2 in bo:
        print([x, int(x + (Sb - Sa) / 2)])