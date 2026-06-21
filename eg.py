class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return f"{self.name} makes sound"
class Dog(Animal):
    def __init__(self,name,breed):
        super(). __init__(name)
        self.breed=breed
    def speak(self):
        return f"{super().speak()}and barks"
dog=Dog("tommy","Gloden Retviler")
print(dog.speak())        