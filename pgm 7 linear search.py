l=eval(input('enter the list:'))
length=len(l)
element=int(input('enter the element to be searched for:'))
for i in range(0,length):
    if(l[i]==element):
        print('the element found at index',i)
        break
else:
    print('element not found')
  
