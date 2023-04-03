#return as array
x=[]
def subseq(p,up):

    if len(up)==0:
        x.append(p)
        return x
    ch=up[0]
    subseq(p+ch,up[1:])
    subseq(p,up[1:])
    return x

print(subseq('','abc'))