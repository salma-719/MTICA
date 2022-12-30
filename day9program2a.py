def printSeriesDecreasing(ch,n):
    assert isinstance(ch,str),'first argument should be string'
    assert isinstance(n,int),'second argument should be integer'
    for i in range(n,0,-1):
        print(ch*i) 
    return None

inpch=input("Enter a character:")
inpnum=int(input("Enter a no:"))
print('_'*40)
try:
    printSeriesDecreasing(inpch,inpnum)
except AssertionError as ob:
        print(ob)
