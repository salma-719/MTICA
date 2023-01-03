class Number:
    def __init__(self,n):
        self.n=n
    def calculateFactorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n +1):
            res *=i
        return res
    def checkArmstrong(self):
        assert self.n>=0,'The number should be >=0'
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)**len(temp)
        if t==self.n:
            return 'Armstrong'
        else:
            return 'Not Armstrong'

    
inp=int(input())
obj=Number(inp)
print('Factorial of',inp,'is',obj.calculateFactorial())
##print(inp,"is",obj.checkArmstrong())

try:
    print(inp,'is',obj.checkArmstrong())
except AssertionError as a:
    print(a)
##print('sum of Digits of',inp,'is',obj.sumOfDigits())
