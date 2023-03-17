def pernum(num):
    divsum=0
    for i in range(1,num):
        if num%i==0:
            divsum+=i
    if divsum==num:
        print("perfect no")
    else:
        print("not a perfect no")
pernum(6)
pernum(15)
