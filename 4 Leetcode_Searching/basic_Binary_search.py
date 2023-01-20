a=[1,2,3,4,5,6,7,8,9,10,11]

t=9

x=len(a)
l=1
r=x-1



while l<r:
       m=int((l+r)/2)
       if a[m]==t:
            print(m)
       if a[m]>t: #go left
           r=m
       else: # go right
           l=m

        