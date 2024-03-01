#!/usr/bin/env python
program_description = """A simple python script to print lines that match 
a substring in a large file.
"""

def search(substring, filename):
    with open(filename) as infile:
        for n, line in enumerate(infile, 1):
            if substring in line:
                print(n, line)



if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description=program_description)
    parser.add_argument("search", type=str, help="search string")
    parser.add_argument("filename", type=str, help="filename to parse")
    args = parser.parse_args()

    search(args.search, args.filename)