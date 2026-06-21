class Student_marks:
    def __init__(self,name,eng,maths,science):
        self.name=name
        self.eng=eng
        self.maths=maths
        self.science=science
    def Calculate_marks(self):
        total=self.eng+self.maths+self.science
        count=total/300*100
        print("congratulation",self.name,"your total percentage is",count)
S1=Student_marks("Shyam",89,90,91)
S1.Calculate_marks()            



