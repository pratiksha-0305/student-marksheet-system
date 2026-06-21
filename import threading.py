import threading
import time
def square(num):
    print(f"Square: {num*num}")
    time.sleep(5)
def cube(num):
    print(f"Cube: {num*num*num}")
    time.sleep(5)

t1 = threading.Thread(target=square, args=(2,))
t2 = threading.Thread(target=cube, args=(4,))

t2.start()
t1.start()
t1.join()
t2.join()
print("Done!")