# Calculate Distance Between Two Points

import math
x1=int(input("Give x1: "))
x2=int(input("Give x2: "))
print("first point is: ("+str(x1)+","+str(x2)+")")


y1=int(input("Give y1: "))
y2=int(input("Give y2: "))
print("2nd point is: ("+str(y1)+","+str(y2)+")")


d=math.sqrt((x2-x1)**2+(y2-y1)**2)

print("The distance is:"+str(d))