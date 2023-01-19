# Write a function to find if a number is a palindrome or not. Take number as parameter


def palindromeOrNot(x):
        
        y=[]
        for n in range(len(x)):
            m=x[n]
            y.append(m)

            
        r=[]
        for i in range(len(y),0,-1):
            r.append(y[i-1])

 

        p=r[0]
        for n in range(1,len(r),1):
                p=p+r[n]

        a=int(p)
        if a==int(x):
            print('Palindrome')
        else:
            print('Not Palindrome')   


x=input("Take the number: ")
palindromeOrNot(x)