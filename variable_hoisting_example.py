def testfn():
    global a
    a = 200

testfn()
print(f"In main: {a=}")
