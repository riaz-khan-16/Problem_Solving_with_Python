# 13. [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/)
# creative

#Method-1 
# Time O(N)  Space O(1)

# n=25689
# r=[]

# while n>0:
#     x=(n-1)%26
#     n=(n-1)//26 
#     r.append((x))

# a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# for i in range(len(r)):
#     r[i]=a[r[i]]

# r.reverse()
# r=''.join(r)
# print(r)


#Method-2
# Time O(Log N)  Space O(1)

n=25689
r=[]

while n>0:
    x=(n-1)%26
    n=(n-1)//26
    r.append(chr(x+65))


r.reverse()
r=''.join(r)
print(r)


# methid-3

# def convertToTitle(columnNumber):
#         r = ''
#         d = ord('A') 
#         n=columnNumber
#         while n > 0:
#             y = (n-1) % 26
#             n = (n-1) // 26
#             s = chr(y+d)
#             r = ''.join((s, r))

#         return (r)
# print(convertToTitle(25689))

