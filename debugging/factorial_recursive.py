#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <entier_non_negatif>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Erreur : l'argument doit être un entier.")
        sys.exit(1)
    
    try:
        f = factorial(n)
    except ValueError as e:
        print(e)
        sys.exit(1)

    print(f)

if __name__ == "__main__":
    main()