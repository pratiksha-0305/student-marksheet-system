def process(filename):
    try:
        with open(filename,"r") as file:
            data=file.read()
            print(data)
    except FileNotFoundError as e:
        print(f"file not found:{filename}")
        raise
try:
    process("C:\\Users\\ACER\\Desktop\\txt.doc\\student.txt.txt")
except FileNotFoundError as e:
    print("doesn't exist")
'''else:
    print("file found")
finally:
    print("code run succesfully")'''        