import argparse

parser = argparse.ArgumentParser(description="Find hcf (gcd) of two given integers.")
parser.add_argument("a", type=int, help="first number")
parser.add_argument("b", type=int, help="second number")
args = parser.parse_args()

a, b = args.a, args.b

while b:
    a, b = b, a % b

print(a)
