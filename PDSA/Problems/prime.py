from math import sqrt
def isPrime(n):
    i = 1
    while i<=sqrt(n):
        if n%i==0:
            return False
        i+=1
    return True
isPrime(13)