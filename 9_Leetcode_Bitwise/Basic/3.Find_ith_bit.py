
i=4

def find(i):
    
    b=11111011110
    m=1<<i-1
    x= b & m
    return x

print(find(6))