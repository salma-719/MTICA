def patternPrinting(s,n):
    assert(n>=0), 'INVALID'
    for i in range(n,0,-1):
        print(s*i)
s=input()
n=int(input())
try:
    patternPrinting(s,n)
except AssetionError as a:
    print(a)
