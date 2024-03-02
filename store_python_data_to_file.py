a = 100
b = False
c = 4.5
d = None
e = (11, 22, 33, 44)
f = [65, (33, 22, 66), [11, 23, 45]]
g = {
    "hosts": ["localhost", "192.168.1.1"],
    "port": 4567,
    "users": {
        "jane": "developer",
        "charles": "developer",
        "sam": "admin"
    } 
}

with open("data.dat", "w") as outfile:
        print(a, b, c, d, e, f, g, sep="\n", file=outfile)
        
