def printSeriesDecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpch=input("Enter a character:")
inpnum=int(input("Enter a no:"))
print('_'*40)
printSeriesDecreasing(inpch,inpnum)
