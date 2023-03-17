def bsearch(list,beg,end,it):
    while beg<=end:
        mid=int((beg+end)/2)
        if(list[mid]==it):
           return mid
        elif(list[mid]>it):
            end=mid-1
        elif(list[mid]<it):
            beg=mid+1
        else:
            return-1
l=[10,20,30,40,50]
beg=0
end=len(l)-1
print('enter the item to be searched for')
it=int(input("enter"))
result=bsearch(l,beg,end,it)
if(result==-1):
    print('item not found')
else:
    print('item found at index',result)


        
