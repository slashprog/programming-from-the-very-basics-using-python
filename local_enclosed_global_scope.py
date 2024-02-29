a = 100

def testfn():
    a = 200  # Enclosed-variable
    def foo():
        a = 300 # Local-variable
        print("In testfn: a =", a)

    foo()


testfn()

