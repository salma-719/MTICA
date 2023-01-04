def printWeek(dn):
    if (dn==1):
        return 'Sunday'
    if (dn==2):
        return 'Monday'
    if (dn==3):
        return 'Tuesday'
    if (dn==4):
        return 'Wednesday'
    if (dn==5):
        return 'Thursday'
    if (dn==6):
        return 'Friday'
    if (dn==7):
        return 'Saturday'
    else:
        return 'INVALID'
for i in range(1):
    inpnum=int(input())
    print(printWeek(inpnum))
