"""provides useful math utility functions
   
This module provides functions to find gcd, generate
fibonacci series, check for prime numbers and so on...   
"""

def fibonacci(n):
    """Generate the first 'n' fibonacci series"""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

def hcf(x, y):
    """Returns the HCF of x and y passed as arguments"""
    while y:
        x, y = y, x % y
    return x