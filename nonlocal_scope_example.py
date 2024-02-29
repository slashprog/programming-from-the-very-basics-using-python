a = 100

def testfn():
    a = 200  # Enclosed-variable
    def foo():
        nonlocal a
        #global a
        a = 300 # Local-variable
        print("In foo: a =", a)
    foo()
    print("In testfn: a =", a)


testfn()
print("In main: a =", a)

