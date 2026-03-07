class Animal:

    def sound(self):
        print("some generic animal sound.")



animal = Animal()
print (animal.sound())


class Dog(Animal):
    def sound(self):
        print("Woof!")


dog = Dog()
print(dog.sound())


class Cat(Animal):
    def sound(self):
        print("Meow!")

cat = Cat()
print(cat.sound())
