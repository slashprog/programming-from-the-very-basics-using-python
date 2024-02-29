a = [100, 200, 300]

def testfn():
    print(f"In testfn(): {a=}") # global-scope
    a[0] = 111 # This is NOT variable re-assignment, but a form of object mutation
    #a = [111, 200, 300]

testfn()
print(f"In main: {a=}")
