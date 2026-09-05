class Vehicle:
    def __init__(self,make,model,year_of_production):
        self.make=make
        self.model=model
        self.year_of_production=year_of_production

    def __repr__(self):
        return f'Make: {self.make}, Model:{self.model}, Year{self.year_of_production}'


class Car(Vehicle):
    def __init__(self,make,model,year_of_production,color):
        super().__init__(make,model,year_of_production)
        self.color=color

    def __repr__(self):
        return f'{super().__repr__()},Color:{self.color}'


class ElectricCar(Vehicle):
    def __init__(self,make,model,year_of_production,battery_capacity):
        super().__init__(make,model,year_of_production,)
        self.battery_capacity=battery_capacity

    def battery_charging(self):
        print("Charging the battery until: ",self.battery_capacity)

    def __repr__(self):
        return f'this is an electric car: {super().__repr__()}.'


def main():
    tesla:ElectricCar=ElectricCar("Tesla", "X", 2023, 600)
    tesla.battery_charging()
    print(tesla)

if __name__=="__main__":
    main()