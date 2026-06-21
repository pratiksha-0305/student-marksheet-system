def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print("ZeroDivisionError.trying to handle")
        try:
            raise ValueError("Handling error failed with a value error")
        except ValueError as ve:
            print(f"valueError:{ve}")
            raise RuntimeError("failed to handle an error due to nestd exception")
def process():
    try:
        result=divide(10,2)
        print(f"result={result}")
    except RuntimeError as e:
        print(f"final output:{e}")
        print(f"output:{e}")   
process()                 