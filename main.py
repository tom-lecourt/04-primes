"""
Main script for knowing if a number is prime or not
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """Show if a number is prime or not.
    Args:
        p (float) : the chosen number.
    Returns:
        boolean: result if he is prime or not.
    """

    if p < 2:
        return False
    if p == 2:
        return True
    # Check if n is divisible by any number from 2 to sqrt(n)
    for i in range(2, int(sqrt(p))):
        if p % i == 0:
            return False
    return True

#### Fonction principale


def main():
    """main function 
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
