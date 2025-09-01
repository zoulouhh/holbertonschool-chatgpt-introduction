#!/usr/bin/python3
import sys

def factorial(n):
    """Calcule le factoriel de n (n!)."""
    if n < 0:
        raise ValueError("Le factoriel n'est pas défini pour les nombres négatifs.")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Il faut décrémenter n à chaque itération
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <entier>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        f = factorial(n)
        print(f"Le factoriel de {n} est {f}")
    except ValueError as e:
        print("Erreur :", e)
        sys.exit(1)