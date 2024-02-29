def testfn():
    a = 200
    def foo():
        print("In foo: a =", a)
    return foo

fn = testfn()  # Accessor pattern
fn()

