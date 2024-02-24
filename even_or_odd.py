import argparse

parser = argparse.ArgumentParser()
parser.add_argument("number", type=int, help="input number that needs to be checked")

args = parser.parse_args()

even_or_odd = "even" if args.number % 2 == 0 else "odd"
print(args.number, "is an", even_or_odd, "number")
