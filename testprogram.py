user = "John Doe"
score = 67

import time

def square(x):
    return x*x

def run():
    print("user =", user, "score =", score)
    print("Time now is", time.ctime())
    print("Square of 2 is", square(2))
    print("testprogram.py is running as", __name__, "module")
    print(globals())
    
if __name__ == '__main__':
    run()