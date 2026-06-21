class Animal:
    def __init__(self,name):
        self.name=name
    def Move(self):
        return f"{self.name} Move"
    def Speak(self):
        return f"{self.name} makes a sound"
class Dog(Animal):
    def Speak(self):
        return f"{self.name}barks"
class Cat (Animal):
    def Speak(self):
        return f"{self.name}meow"
dog1=Dog("Tommy")
print(dog1.Speak())
print(dog1.Move())
cat1=Cat("kitty")
print(cat1.Move())
print(cat1.Speak())   


