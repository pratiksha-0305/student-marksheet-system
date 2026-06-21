class Pet_Animals:
    def animal(self):
        print(" These are pet animals")
class Cat(Pet_Animals):
    def cat(self):
        print("Cat is pet animal")
class Dog(Pet_Animals):
    def dog(self):
        print("Dog is pet animal") 
d=Dog()
d.dog()
d.animal()               