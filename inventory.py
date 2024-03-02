def read_csv(filename):
    with open("inventory.csv") as inv:
        headers = [field.strip('"') \
                   for field in inv.readline().rstrip().split(",")]
        
        csv = {}
        for line in inv:
            for key, value in zip(headers, line.rstrip().split(",")):
                value = value.strip('"')
                value = int(value) if value.isdecimal() else value
                csv.setdefault(key, []).append(value)
        
        return csv
        
if __name__ == '__main__':
    info = read_csv("inventory.csv")
    print(info)
