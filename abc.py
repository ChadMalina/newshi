from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def brake(self):
        pass


class Car(Vehicle):
    def __init__(self, make):
        self.make=make
    def brake(self):
        return f"{self.make} has stopped!"
    def move(self):
        return f"{self.make} has moved!"
car1=Car("Nissan")
print(car1)
print(car1.brake())
print(car1.move())