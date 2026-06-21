def divide_number(a,b):
    if b ==0:
        raise ZeroDivisionError("you cannot divide by zero")
    return a/b
try:
    result=divide_number(10,0)
    #print("result=",result)
except ZeroDivisionError as e:
    print(f"Error:{e}")    #f=formated string 