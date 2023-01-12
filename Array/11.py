#Leetcode 1773: Count Items Matching a Rule

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]

ruleKey="color"
ruleValue = "silver"

if ruleKey=="color":
    i=1
elif ruleKey=="type":
    i=0
else:
    i=2  
a=0
for j in range(len(items)):
    if items[i][j]==ruleValue: 
       a=a+1 
print(a)
