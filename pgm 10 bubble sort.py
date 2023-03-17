l=[3,10,75,84,2,36,12]
print('original list:',l)
n=len(l)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print('the sorted list is:',l)
        
