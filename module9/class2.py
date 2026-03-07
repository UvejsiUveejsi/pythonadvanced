class Animal:
    def __init__(self, name):
        self.name = name


    def sound(self):
        print("animal sound")

    def description(self):
        print(f"this is an animal named {self.name}")



class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


    def sound(self):
        super().sound()

        print("auuuuuuu")

    def description(self):
        super().description()
        print(f"breed: {self.breed}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color =color

    def sound(self):
            super().sound()

            print("miow")

    def description(self):
            super().description()
            print(f"color: {self.color}")

animal = Animal("Generic ")
print(animal.sound())
print(animal.description())


dog = Dog("rex", "golden retriever")
print(dog.sound())
print(dog.description())

cat = Cat("whiskers", "white")
print(cat.sound())
print(cat.description())
