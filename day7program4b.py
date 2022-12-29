ans=[ [i,max([j for j in range(1,11)if i%j==0 ])]
      for i in range(100,110) ]
print(ans)
