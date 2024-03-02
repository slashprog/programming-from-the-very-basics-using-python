var_names = "a", "b", "c", "d", "e", "f", "g"

with open("data.dat") as infile:
    for var, line in zip(var_names, infile):
        globals()[var] = eval(line)
    
for v in a, b, c, d, e, f, g:
    print(v, type(v))
