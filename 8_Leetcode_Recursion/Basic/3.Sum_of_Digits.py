x=12564

def find(x):

    if x==0:
        return 0
    f=find(x//10)+x%10
    return f

print(find(x))