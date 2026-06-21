def prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        print("Not Prime")
        return
    # Check divisibility from 2 to n-1
    for i in range(2, n):

        # If n is divisible by i, it is not prime
        if n % i == 0:
            print("Not Prime")
            return

    # If no divisor is found, the number is prime
    print("Prime")
num = int(input("Enter a number: "))
prime(num) # Call the function