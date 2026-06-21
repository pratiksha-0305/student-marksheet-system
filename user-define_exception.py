class DefineAge(Exception):
    def __init__(self,age,message="Age must be between 1 and 60"):
        self.age=age
        self.message=message
        super().__init__(self.message)
    def __str__(self):
        return f"{self.age}:{self.message}"
def CheckAge(age):
    if age < 1 or age > 60:
        raise DefineAge(age)  
    else:
        print(f"age {age} is within the valid range.")
try:
    CheckAge(65)
except DefineAge as e:
    print(f"Error is {e}")
   
