#!usr/bin/env python3


def decimalToBinary(n: int) -> int:
    return "{0:b}".format(int(n))


def palindrom_2szamr() -> int:
    result: int = 0
    for i in range(1000000):
        if (
            str(i) == str(i)[::-1]
            and str(decimalToBinary(i)) == str(decimalToBinary(i))[::-1]
        ):
            result += i
    return result


def main():
    print(palindrom_2szamr())


if __name__ == "__main__":
    main()
