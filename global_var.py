a = 100

def testfn():
    print(f"In testfn(): {a=}") # global-scope

testfn()
print(f"In main: {a=}")
