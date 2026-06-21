from abc import ABC,abstractmethod
#abstrat class
class Login(ABC):
    @abstractmethod
    def loginn(self):
        pass
    # child class
class User(Login):
    def __init__(self,username,password):
        self.username=username   
        self.password=password
    def loginn(self):
        if self.username == "pratiksha" and self.password == "1234":

            print("login successful")
        else:
            print("invalid password and user name")
            

U1=User("pratiksha","1234")
U1.loginn()
            
        
        
   