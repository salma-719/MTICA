import math
n=input()
total=0
for i in n:
    total +=math.pow(int(i),len(n))
if int(n)==total:
    print(n,"is Armstrong number")
else:
    print("n,is not Armstrong number")
