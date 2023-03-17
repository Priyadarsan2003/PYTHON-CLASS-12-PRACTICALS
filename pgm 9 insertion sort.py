l=[20,85,74,36,25,84,96]
print('original list is:',l)
n=len(l)
for i in range(1,n):
    k=l[i]
    j=i-1
    while j>=0 and k<=l[j]:
        l[j+1]=l[j]
        j=j-1
    else:
        l[j+1]=k
print('the sorted list is',l)        
