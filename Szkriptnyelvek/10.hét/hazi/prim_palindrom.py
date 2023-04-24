#!usr/bin/env python3


def is_palindrom(num: int) -> bool:
    orig_num = str(num)
    if orig_num == orig_num[::-1]:
        return True
    else:
        return False


def is_prime(n: int) -> bool:
    """
    Decide whether a number is prime or not.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    maxi = n**0.5 + 1
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2

    return True


def palin_prim(number: int) -> int:
    M = number
    while M >= number:
        if is_prime(M) and is_palindrom(M):
            break
        else:
            M += 1
    return M


def main():
    print(palin_prim(31))
    print(palin_prim(130))
    print(palin_prim(131))
    print(palin_prim(1977))


if __name__ == "__main__":
    main()
