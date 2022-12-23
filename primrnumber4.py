import day1program4
start=int(input())
stop=int(input())
lst=[]
for i in range(start,stop+1):
    if day1program4.checkPrimeNumber(i):
        lst.append(i)
print(*lst)
print(len(lst))
