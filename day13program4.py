def printSun():
    print("Sunday")
def printMon():
    print("Monday")
def printTue():
    print("Tuesday")
def printWed():
    print("Wednesday")
def printThu():
    print("Thursday")
def printFri():
    print("Friday")
def printSat():
    print("Saturday")
def choose():
    print("Enter day number between 1-7")
    return
dayDict={ 1: printSun ,2: printMon, 3:printTue, 4:printWed,
         5:printThu, 6:printFri, 7:printSat}
choose()
inpNum=int(input())
if inpNum>1 and inpNum<=7:
    dayDict[inpNum]()
else:
    print("INVALID")
    
