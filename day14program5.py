class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color

class cat(Animal):
    def mew(self):
        print("Cat meows")
class Dog(Animal):
    def bark(self):
        print("Woof")

if __name__=="__main__":
    print(__name__)
    pet1=Dog("tomy","brown")
    pet2=cat("lucy","white")
    pet1.bark()
    pet2.mew()
    print(pet1.name)
    print(pet2.name)
