
class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity


    def seating_capacity(self, capacity):

        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage, capacity)

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

    def fare(self):
        return super().fare() * (1 + 0.1)

    def which_clas(self):
        return type(self)
class Car(Vehicle):
    pass
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    modelX = Vehicle('ABCD', 240, 18, 45)
    print(modelX.max_speed, modelX.mileage)
    modelB = Bus('BUS1', 240, 18, 50)
    print(f'Color: {modelB.color},Vehicle Name: {modelB.name}  Speed : {modelB.max_speed}  Mileage : {modelB.mileage}')
    print(modelB.seating_capacity())
    modelC = Car('Audi Q5', 240, 18, 4)
    print(f'Color: {modelC.color}, Vehicle name: {modelC.name}, Speed: {modelC.max_speed}, Mileage: {modelC.mileage}')
    School_bus = Bus("School Volvo", 240, 12, 50)
    print(f'Total bus fare is {School_bus.fare()}')
    print(School_bus.which_clas())
    print(isinstance(School_bus, Vehicle))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
