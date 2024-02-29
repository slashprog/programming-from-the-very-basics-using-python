a = 100

def testfn():
    print(f"In testfn(): {a=}") # global-scope
    a = 200

testfn()
print(f"In main: {a=}")
