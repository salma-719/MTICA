def checkPrimeNumber(num):
    if num<1:
        return 0
    if num==1 or num==2 or num==3:
        return num
    count=num//2+1
    for i in range(2,count):
        if num%i==0:
            return 0
    return num
inpnum=int(input("enter a number:"))
if checkPrimeNumber(inpnum):
    print(inpnum,"is a prime number.")
else:
    print(inpnum,"is not a prime number.")
