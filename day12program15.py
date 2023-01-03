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
    def checkPrime(self):
        assert (self.n>=0),"Not valid"
        if (self.n==1 or self.n==2 or self.n==3):
            return "prime"
        for i in range(2,self.n):
            if self.n % i==0:
                return "Not prime"
        return "prime"
        
    
inp=int(input())
obj=Number(inp)
print('Factorial of',inp,'is',obj.calculateFactorial())
##print(inp,"is",obj.checkArmstrong())

try:
    print(inp,'is',obj.checkArmstrong())
except AssertionError as a:
    print(a)
##print('sum of Digits of',inp,'is',obj.sumOfDigits())
