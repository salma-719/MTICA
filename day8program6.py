num1=input("Enter a number:")
num2=input("Enter a number:")

try:
    res=int(num1)/int(num2) #Excecute with num2=non zero and zero #4
except ZeroDivisionError:
    print("Exception handled by Manohar")
except ValueError:
    print("Exception handled by Gangully")
except Exception as ob:
    print (ob)
else:
    print (num1, '/',num2, '=',res)
finally:
    print("Thanks")
    
print("visit again at python class at MTICA")
