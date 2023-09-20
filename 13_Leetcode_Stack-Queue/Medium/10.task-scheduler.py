# 10. [Task Scheduler](https://leetcode.com/problems/task-scheduler/) leetcode


    
tasks = tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
n = 2

if n==0:
    print(len(tasks))

# highest frequency finding
F=[]
for i in range(ord('A'),ord('Z')):
          x=chr(i)
          F.append(tasks.count(x))
HF=max(F)          

CHF=F.count(HF)

chunk=HF-1


result=chunk*(n+1)+CHF
print(max(result,len(tasks)))


#find same  highest frequency character




    




    
    




