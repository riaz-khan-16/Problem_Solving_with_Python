
string='ajdkapplejfk'
word='apple'


def f(news,mains):

    if len(mains)==0:
        return news
    ch=mains[0:5]
    if ch=='apple':
         return news+mains[5:]
    else:
        return f(news+ch[0],mains[1:])
   

print(f('','ajdkapplejfk'))






