# Maximum Population Year
# https://leetcode.com/problems/maximum-population-year/
# Input: logs = [[1993,1999],[2000,2010]]
# Output: 1993

logs = [[1950,1961],[1960,1971],[1970,1981]]

#create an array for years from 1950 to 2050
#fill 1 for alive
#find maximum alive year
#find is there any match
#find earlier year


#create an array for years from 1950 to 2050
t=[]
for i in range(0,101,1):
      t.append(0)
# print(t)       
# print(len(t))  

#fill 1 for alive
for a in logs:
    a=a
    for j in range(a[0],(a[1]),1):
        j=j-1950
        t[j]=t[j]+1
print(t)

#find maximum alive year
m=max(t)
print(m)

#find is there any match
my=[]
for i in range(len(t)):
    if t[i]==m:
        i=i+1950
        my.append(i)
print(my)

#find earlier year
mp=min(my)
print(mp)
