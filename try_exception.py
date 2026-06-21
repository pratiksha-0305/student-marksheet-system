a=10
b=2
try:
    result=a/b
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("result is",result)
finally:
    print("program execution completed")