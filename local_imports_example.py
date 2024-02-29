def testfn():
    import time
    print(f"In testfn(): time = {time.ctime()}")

testfn()
print("In main: time =", time.ctime())