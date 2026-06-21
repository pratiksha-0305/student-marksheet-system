#format for strftime
#strftime:Convert date and time into readable form
import datetime
x=datetime.datetime.now() # gives current date and time
print(x.strftime("%A")) # full weekday name (wednesday)
print(x)

x=datetime.datetime.now()
print(x.strftime("%a")) # short weekday name (wed)
print(x)

x=datetime.datetime.now()
print(x.strftime("%B")) #Full month name (january)
print(x)

x=datetime.datetime.now()
print(x.strftime("%b")) # short month name(jan)
print(x)
                 
x=datetime.datetime.now()
print(x.strftime("%w")) #weekday as number(0-6) if sun then it will 0
print(x)

x=datetime.datetime.now()
print(x.strftime("%d")) # day of month
print(x)

x=datetime.datetime.now()
print(x.strftime("%m")) # month as number(01-12) if may then it will 05
print(x)

x=datetime.datetime.now()
print(x.strftime("%Y")) # full year format (2026)
print(x)

x=datetime.datetime.now()
print(x.strftime("%y")) # short year format (26)
print(x)

x=datetime.datetime.now()
print(x.strftime("%H")) # hours in 24-hr format
print(x)

x=datetime.datetime.now()
print(x.strftime("%I")) # hours in 12-hr format
print(x)

x=datetime.datetime.now()
print(x.strftime("%p")) # show AM or PM
print(x)

x=datetime.datetime.now()
print(x.strftime("%M")) #Minutes value
print(x)
      
x=datetime.datetime.now()
print(x.strftime("%S")) # Second value
print(x)
            
      
      
      
