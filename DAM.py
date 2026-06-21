class Demo_acces_modifiers:

    def __init__(self, public, private, protected):
        self.public = public
        self.__private = private
        self._protected = protected

    def show(self):
        return {
            "public": self.public,
            "private": self.__private,
            "protected": self._protected,
        }


DAM = Demo_acces_modifiers(10, 20, 30) # creating object

print(DAM.public)

 #print(DAM.__private)   # Errro

print(DAM._protected)

print(DAM._Demo_acces_modifiers__private)

print(DAM.show())