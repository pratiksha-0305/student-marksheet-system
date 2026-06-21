# Student Marksheet System
#file=open("C:\\Users\\ACER\\Desktop\\pratiksha.python\\mini_project.py")
while True:
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")

    sub1 = float(input("Enter marks of English: "))
    sub2 = float(input("Enter marks of physic: "))
    sub3 = float(input("Enter marks of Chemistry : "))
    sub4 = float(input("Enter marks of maths:"))
    sub5 = float(input("Enter marks of biology: "))

    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"

    print("*****STUDENT MARKSHEET*****")
    print("Student Name :", name)
    print("Roll Number  :", roll_no)
    print("Total Marks  :", total) 
    print("Percentage   :", round(percentage, 2), "%")
    print("Grade        :", grade)
    if grade=="A+" or grade=="A" or grade=="B" or grade=="C" or grade=="D":
        print(f"Congratulations! {name}, you got {percentage:.2f}%")
    else:
        print("better luck next time")   
    print("============================") 