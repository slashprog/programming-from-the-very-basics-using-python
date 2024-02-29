def testfn():
    def foo():
        print("This is foo()!")
    print("In testfn:")
    foo()
    foo()
    foo()


testfn()
foo()