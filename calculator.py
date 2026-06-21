class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

C1 = Calculator(10, 5)

print("Addition:", C1.a + C1.b)
print("Subtraction:", C1.a - C1.b)
print("Multiplication:", C1.a * C1.b)
print("Division:", C1.a / C1.b)