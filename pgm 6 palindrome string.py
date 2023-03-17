msg=input('enter any string:')
newlist=[]
newlist[:0]=msg
l=len(newlist)
ed=l-1
for i in range(0,l):
    if newlist[i]!=newlist[ed]:
        print('given string is not a palindrome')
        break
    if i>=ed:
        print('given string is a palindrome')
        break
    l=l-1
    ed=ed-1
