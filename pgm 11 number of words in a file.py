f=open('count.txt')
l=f.read()
r=l.split()
count=0
for i in r:
    count+=1
print('no of words=',count)    
