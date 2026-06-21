#name="jhon"
a=20
b=0
try:
    result= a/b
except ZeroDivisionError:
    print("you cannot divid by zero") 
except ValueError:
    print("invalid value")
except Exception as e:
    print("error occured",e)
else:
    print("result is",result)
finally:
    print("program run succesfully")                   