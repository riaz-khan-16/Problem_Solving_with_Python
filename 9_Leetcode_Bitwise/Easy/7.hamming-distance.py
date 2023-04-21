# 7. [Hamming Distance](https://leetcode.com/problems/hamming-distance/)

x = 3
y = 1

def decimal_to_binary(n):
    ans=''
    while n>0:
        last=n%2
        n=n//2
        ans=str(last)+ans
    return ans
x=decimal_to_binary(x^y)
print(x.count('1'))





