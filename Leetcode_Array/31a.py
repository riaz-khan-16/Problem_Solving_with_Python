

#Given that:
rows = 5
cols = 6
rStart = 1
cStart = 4

ans=[]
left=cStart
right=cStart+1
top=rStart
bottom=rStart+1


for i in range(left,right):
          ans.append([top,i])
left -= 1


for i in range(top,bottom):
          ans.append([i,right])
top -=1


for i in range(right,left,-1):
          ans.append([bottom,i])     

right+=1


 
for i in range(bottom,top,-1):
          ans.append([i,left])                 
bottom+=1


print(ans)          