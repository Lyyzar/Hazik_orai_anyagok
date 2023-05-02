#!usr/bin/env python3


class Verem:
    def __init__(self):
        self.verem = []

    def __str__(self):
        res = "["
        for e in self.verem:
            res += str(e) + ", "
        return res

    def meret(self):
        return len(self.verem)

    def ures(self):
        if not self.verem:
            return True
        else:
            return False

    def betesz(self, num):
        self.verem.append(num)

    def kivesz(self):
        if not self.verem:
            return None
        else:
            return self.verem.pop()


def main():
    v = Verem()
    print(v)  # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)  # [1 4 5
    print(v.meret())  # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)  # 1
    print(v)  # [1 4
    v.kivesz()
    v.kivesz()  # most már üres
    x = v.kivesz()
    print(x)  # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)


if __name__ == "__main__":
    main()
