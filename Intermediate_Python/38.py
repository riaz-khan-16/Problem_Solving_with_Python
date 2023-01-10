# Write a function to check if a given triplet is a Pythagorean triplet or not


def isPythagorean(a,b,c): 
        
            if a==b or c==b or c==a:
                return False
            elif a==c==b:
                return False    

            def findMax(a,b,c):
                if a>b and a>c :
                    return a
                elif b>a and b>c:
                    return b
                elif c>a and c>b:
                    return c       
            def findMin(a,b,c):
                if a<b and a<c :
                    return a
                elif b<a and b<c:
                    return b
                elif c<a and c<b:
                    return c

            def findMiddle(max,min,a,b,c):
                if max>a>min:
                    return a
                elif max>b>min:
                    return b    
                elif max>c>min:
                    return c     

            max=findMax(a,b,c)
            min=findMin(a,b,c)
            middle=findMiddle(max,min,a,b,c)
            
            if max**2==min**2+middle**2:
                  return True
            else:      
                  return False      

a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

if isPythagorean(a,b,c):
    print("Pythagorean")
else:   
    print("Not Pythagorean") 
