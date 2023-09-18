class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("dog, barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animal1=Animal()
animal2=Dog()
animal3=Cat()

animal1.sound()
animal2.sound()
animal3.sound()
