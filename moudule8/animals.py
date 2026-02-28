class Animal:
    def __init__(self, typeOfAnimal, raca, color):
        self.typeOfAnimal = typeOfAnimal
        self.raca = raca
        self.color = color

    def greet(self):
        print("the type of animal is", self.typeOfAnimal, "the race is", self.raca, "the color is", self.color)



dog = Animal("dog", "Husky", "white")
cat = Animal("feline", "british", "grey")

print(dog.greet())
print(cat.greet())