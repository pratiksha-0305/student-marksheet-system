class Calculator:
    def add(self, a, b, c=None, d=None):
        if c is None and d is None:
            return a + b
        elif d is None:
            return a + b * c
        else:
            return a + b * c / d

cal=Calculator()
print(cal.add(1,8)) 
print(cal.add(2,6,4))
print(cal.add(3,5,2,10))   