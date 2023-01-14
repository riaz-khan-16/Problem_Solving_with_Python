#Leetcode: 989. Add to Array-Form of Integer

# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234

num = [1,2,0,0]
k = 34

# ArrayToNum
n=''
for i in num:
    i=str(i)
    n=n+i 
print(n)


#add k
n=int(n)+k

print(n)

#NumToArray


n=str(n)
print(n)

a=[]
for i in n:
    a.append(int(i))
print(a)    
