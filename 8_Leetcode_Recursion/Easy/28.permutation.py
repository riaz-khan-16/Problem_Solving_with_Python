

# Input : abc
# Output : a ab abc ac b bc c


a='abc'

def subseq(p,up):

    if len(up)==0:
        print(p)
        return
    ch=up[0]
    subseq(p+ch,up[1:])
    subseq(p,up[1:])

subseq('','abc')
