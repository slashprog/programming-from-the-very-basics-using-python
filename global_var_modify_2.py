a = 100

def testfn():
    a = 200
    print(f"In testfn(): {a=}") # global-scope


testfn()
print(f"In main: {a=}")
