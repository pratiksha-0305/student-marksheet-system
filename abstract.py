from abc import ABC,abstractmethod
class Car(ABC):   # parent class
    @abstractmethod #decoretor
    def milage(self):
        pass
    def display(self):
        print("this is a car")
#normal method

class Tesla(Car): #child class
    def milage(self):
        print("Tesla gives 20km range per charge")     
t=Tesla()
t.display()
t.milage()          