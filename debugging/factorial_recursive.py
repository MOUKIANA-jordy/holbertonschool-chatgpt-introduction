#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return "Erreur : Le factoriel n'est défini que pour les entiers positifs."
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) != 2:
    print("Usage: ./script.py <nombre>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
except ValueError:
    print("Erreur : Veuillez fournir un nombre entier.")
    sys.exit(1)

result = factorial(number)
print(result)
