# 4. [First Uppercase Letter in a String](https://www.geeksforgeeks.org/first-uppercase-letter-in-a-string-iterative-and-recursive/) GFG
#First uppercase letter in a string (Iterative and Recursive)


# Input : geeksforgeeKs
# Output : K

a='geeksForgeeKs'

def findUpper(a,i):

    if i==len(a):
        return 'No Upper'
    if a[i].isupper():
        return a[i]
    
    return   findUpper(a,i+1)


print(findUpper(a,0))