#!usr/bin/env python3
import math


class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Ellipse({a},{b})".format(a=self.a, b=self.b)

    def terulet(self):
        return self.a * self.b * math.pi

    def kerulet(self):
        return math.pi * (
            3 * (self.a * self.b)
            - math.sqrt(((3 * self.a) + self.b) * (self.a + 3 * self.b))
        )


def main():
    e1 = Ellipse(10, 13)
    e2 = Ellipse(53, 25)
    print(e1.terulet())
    print(e2.kerulet())
    print(e1)


if __name__ == "__main__":
    main()
