# 5. [Counting Bits](https://leetcode.com/problems/counting-bits/)


# way 1:

def f1(n):
    def decimal_to_binary(n):
        ans=''
        while n>0:
            last=n%2
            n=n//2
            ans=str(last)+ans
        return ans

    n=5
    arr=[]

    for i in range(n+1):
        x=decimal_to_binary(i)
        x=x.count('1')

        arr.append(x)
    return arr 


#way 2


def f2(n):
        
    arr=[]
    for i in range(n+1):
        x=0
        while i>0:
            x=x+i%2
            i=i//2
        arr.append(x)
    return  arr

print(f2(2))





