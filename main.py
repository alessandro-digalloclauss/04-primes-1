from math import sqrt

#### Fonction secondaire


def isprime(p):
    if p <= 1:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True


def main():
    for x in [2, 4, 17, 1, 58]:
        print(f"isprime({x}):", isprime(x))
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


main()
