class Student:   # class name Student

    def __init__(self, name, marks):   # constructor
        self.name = name               # public variable
        self.__marks = marks           # private variable

    def show(self):                    # function name
        print("Name:", self.name)
        print("Marks:", self.__marks)

    def update_marks(self, new_marks):   # function to update marks
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid Marks!")

# creating object of class Student
s1 = Student("Neha", 85)
s1.show()
'''s1.__marks=40" 
 s1.show()  #Error oCCurs'''

# updating marks
s1.update_marks(110)

s1.show()