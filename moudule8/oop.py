class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width


    def calculate_are(self):
        return self.height * self.width

    def calculate_perimiter(self):
        return  2*(self.height * self.width)

new_rectangle = Rectangle(5, 6)

area = new_rectangle.calculate_are()
perimiter = new_rectangle.calculate_perimiter()

print(area)
print(perimiter)
