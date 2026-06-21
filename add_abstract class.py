from abc import ABC,abstractmethod
#abstrat class
class num(ABC):
    @abstractmethod
    def add(self):
        pass
    # child class
class addition(num):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        # implement abstract method
    def add(self):
        output = self.a + self.b
        print("ADDITION = ", output) 
        #object
N1= addition(10,50)
N1.add()           
    