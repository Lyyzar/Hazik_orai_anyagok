#!/usr/bin/env python3

import random

def extended_euclidean_algorithm(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        x, y, z = extended_euclidean_algorithm(b, a % b)
        return (y, x - (a // b) * y, z)


def rsa():
    p=5449      #egyik nagy prím
    q=7757      #másik nagy prím

    n = p * q   #modulus
    phi = (p - 1) * (q - 1)
    good=True


    while good:
        e = random.randrange(2,phi)
        x,y,z = extended_euclidean_algorithm(e,phi)
        if x == 1:
            good = False
    
        


def main():
    print(extended_euclidean_algorithm(280,3))


if __name__=='__main__':
    main()