#Kids With the Greatest Number of Candies
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]

candies = [2,3,5,1,3]
extraCandies = 3

def find():
    o=[]
    premax=max(candies)
    for i in candies:
        maxafter=i+extraCandies
        if maxafter>=premax:
            o.append(True)
        else:
            o.append(False)   
    return o

print(find())
