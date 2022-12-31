fo1=open(r"E:\pythonpractice50\day10\abcd.txt","r")
fo2=open(r"E:\pythonpractice50\day10\abcd.txt","w+")

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("File Copied")
