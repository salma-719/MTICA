inp=input()

##ans=[ ]
##for i in inp:
##    if i in '1234567890':
##        ans.append(i)
##print(*ans)

ans=[i for i in inp if i in '1234567890' ]
print(ans)
