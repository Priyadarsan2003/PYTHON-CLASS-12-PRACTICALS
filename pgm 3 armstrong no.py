no=int(input("enter any number to check:"))
no1=no
sum=0
while(no>0):
    ans=no%10
    sum=sum+(ans*ans*ans)
    no=int(no/10)
if sum==no1:
    print("Armstrong number")
else:
    print("not an Armstrong number")
        
