#!usr/bin/env python3
import math


class Sphere:
    def __init__(self, sugar):
        self.sugar = sugar

    def __str__(self):
        return "Sphere({r})".format(r=self.sugar)

    def felszin(self):
        return 4 * math.pi * self.sugar**2

    def terfogat(self):
        return (4 * math.pi * self.sugar**3) / 3

    def __lt__(self, other):
        return self.sugar < other.sugar

    def __le__(self, other):
        return self.sugar <= other.sugar

    def __gt__(self, other):
        return self.sugar > other.sugar

    def __ge__(self, other):
        return self.sugar >= other.sugar


def main():
    s1 = Sphere(10)
    s2 = Sphere(15)
    s3 = Sphere(10)
    print(s1.felszin())
    print(s2.terfogat())
    print(s1 > s2)
    print(s1 <= s3)
    print(s3)


if __name__ == "__main__":
    main()
