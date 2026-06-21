# Parent class
class Animal:
    def sound(self):
        print("Animals make sounds")


# Child class
class Dog(Animal):
    # Overriding the parent method
    def sound(self):
        print("Dog barks")


# Creating objects
a = Animal()
d = Dog()

# Calling methods
a.sound()   # Parent class method
d.sound()   # Child class overridden method