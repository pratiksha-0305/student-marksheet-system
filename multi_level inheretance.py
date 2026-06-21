class Dog:
    def dog (self):
        print("This is a DOG")
class Cat(Dog):
    def cat(self):
        print("This is a CAt")
class Mouse(Cat):
    def mouse(self):
        print("this is a mouse")        

c=Cat()
c=Dog()
c=Mouse()
c.mouse()
c.cat()
c.dog()
