result=0
val1=float(input("enter the first value:"))
val2=float(input("enter the second value:"))
op=input("enter any one of the operators(+,-,*,/,//,%):")
if op=='+':
    result=val1+val2
elif op=='-':
    result=val1-val2
elif op=='*':
    result=val1*val2
elif op=='/':
    if val2==0:
        print("please enter a value other than 0")
    else:
        result=val1/val2
elif op=='//':
    result=val1//val2
else:
    result=val1%val2
print("the result to",op,"operator:",result)    
