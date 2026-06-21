def largest(a, b, c):
    print("Largest number is:", max(a, b, c))

largest(10, 90, 30)


def largest(a, b, c):
    big = a

    if b > big:
        big = b

    if c > big:
        big = c

    print("Largest number is:", big)


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
largest(x, y, z)