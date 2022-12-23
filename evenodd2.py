def checkEven(n):
    if n<0:
        return "INVALID"
    if inpnum%2==0:
        return"EVEN"
    return"ODD"
inpnum=int(input())
print(checkEven(inpnum))

    
