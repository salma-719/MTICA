fo=open(r"E:\pythonpractice50\day10\abcd.txt","a")
for i in range(5):
    inpstr=input("Enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("written to file")
