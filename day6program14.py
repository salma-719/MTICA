string=input()
ans=[]
wordsList=string.split(' ')
for i in wordsList:
    if len(i)<5:
        ans.append(i)
print(*ans)
        
wordsList=string.split(' ')
ans=[i for i in wordsList if len(i)<5]
print(*ans)

wordsList=string.split(' ')
ans=[i for i in wordsList if len(i)==8 ]
print(*ans)

