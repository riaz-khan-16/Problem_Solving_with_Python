
def f(news,mains):

    if len(mains)==0:
        print(news)
        return 
    ch=mains[0]
    if ch=='a':
         f(news,mains[1:])
    else:
        f(news+ch,mains[1:])

f('','ajkdnfaalda')






