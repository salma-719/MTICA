import sys

print("coming through stdout")

save_stdout = sys.stdout
fh = open(r"d:\mtica\test.txt","w")
sys.stdout = fh
print("This lines goes to test.txt")
print(input())
sys.stdout = save_stdout
fh.close
