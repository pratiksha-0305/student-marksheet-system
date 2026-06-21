import math
class MathematicOperation:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def divide(self):
        try:
            result=self.a/self.b
            print(f"result:{result}")
        except ZeroDivisionError:
            print("you cannot divide by zero")
        except TypeError:
            print("both value must be number")
class SquareOperation(MathematicOperation):
    def __init__(self, a, b):
        super().__init__(a, b)
    def sqrt(self):
        try:
            r1=math.sqrt(self.a)
            r2=math.sqrt(self.b)
            print(f"square of a is:{r1} and square of b is:{r2}")
        except ValueError:
            print("you cannot set square of negative number")
        except TypeError:
            print("both value must me number")
sv=SquareOperation(10,-5)
sv.divide()
sv.sqrt()
op=MathematicOperation(10,0)
op.divide()                                               