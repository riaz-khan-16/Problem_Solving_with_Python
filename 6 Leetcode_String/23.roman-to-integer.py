# 23. [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)



I=1
V=5
X=10
L=50
C=100
D=500
M=1000


s = "MCMXCIV"
x=0
for i in s:
  if i=='I':
    i=1
  if i=='V':
    i=5
  if i=='X':
    i=10
  if i=='L':
    i=50
  if i=='C':
    i=100
  if i=='D':
    i=500
  if i=='M':
    i=1000  
  x=x+i
print(x)  
