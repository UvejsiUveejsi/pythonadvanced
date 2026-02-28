class Person:
    def __init__(self, Emri, Mbiemri, Mosha, Etniciteti, Shoku):
        self.Emri = Emri
        self.Mbiemri = Mbiemri
        self.Mosha = Mosha
        self.Etniciteti = Etniciteti
        self.Shoku = Shoku

    def greet(self):
        print("Emri im eshte", self.Emri, "Mbiemrin e kam", self.Mbiemri, "Me etnicitet jam", self.Etniciteti, "Shoku im eshte", self.Shoku)


Une = Person("Uvejs", "Boro", "12", "Shqiptar","Miloti")

print(Une.greet())