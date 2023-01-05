class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
class Cat(Animal):
    def new(self):
        print("cat meow")
class Dog(Animal):
    def bark(self):
        print("Woof")
if __name__ =='__main__':
    print(__name__)
    pet1=Dog("tomy","brown")
    pet2=Cat("Lilly","Green")
    pet1.bark()
    pet2.new()
    print(pet1.color)
    print(pet2.name)
    print(pet1.name)
    print(pet2.color)
