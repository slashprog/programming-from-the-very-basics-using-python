import testprogram

score = 100

print("This is module_test.py running")
print("In module_test: ", testprogram.user)
print("In module_test: ", testprogram.score)
print("In module_test: ", testprogram.square(3))
print("In module_test: ", testprogram.time.ctime())
print("score =", score)

print("module_test.py is running as", __name__, "module")