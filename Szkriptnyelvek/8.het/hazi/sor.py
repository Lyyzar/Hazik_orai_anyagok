#!usr/bin/env python3


class Sor:
    def __init__(self):
        self.sor:list[int] = []

    def __str__(self):
        res: str = "("
        for e in self.sor:
            res += str(e) + ", "
        return res

    def meret(self) -> int:
        return len(self.sor)

    def ures(self) -> bool:
        if not self.sor:
            return True
        else:
            return False

    def betesz(self, num):
        self.sor.append(num)

    def kivesz(self):
        if not self.sor:
            return None
        else:
            return self.sor.pop(0)


def main():
    v:Sor = Sor()
    print(v)  # (
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)  # (1 4 5
    print(v.meret())  # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)  # 5
    print(v)  # (4 5
    v.kivesz()
    v.kivesz()  # most már üres
    x = v.kivesz()
    print(x)  # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)


if __name__ == "__main__":
    main()
