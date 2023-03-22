n=56432


def rev(n):
    if n==0:
        return ''

    f=str(n%10)+rev(n//10)
    return f

print(rev(n))