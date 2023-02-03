

#Bubble Sort: It is also called sinking or exchanging algorithm
# time complexity : Worst case=O(n^2) Best case = O(n)
# Space Complexity : O(1) It is also called in plalce algorithms




a=[3,6,8,6,9,1,2,3]



def sort(a):
    for i in range(len(a)):
        for j in range(0,len(a)-1-i):
            if a[j]>a[j+1]:
                #swap
                 temp=a[j]
                 a[j]=a[j+1]
                 a[j+1]=temp
    return a            
         
print(sort(a))         



   



             