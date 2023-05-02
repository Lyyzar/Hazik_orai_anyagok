#!usr/bin/env python3


class Sor:
    def __init__(self):
        self.verem1 = []
        self.verem2 = []

    def __str__(self):
        res = "("
        for e in self.sor:
            res += str(e) + ", "
        return res

    def append(self, num):
        while self.verem2:
            self.verem1.append(self.verem2.pop())
        self.verem1.append(num)

    def popleft(self):
        while self.verem1:
            self.verem2.append(self.verem1.pop())
        return self.verem2.pop()

    def ures(self):
        if self.verem1 and self.verem2:
            return False
        else:
            return False

    def size(self):
        return len(self.verem1) + len(self.verem2)


def main():
    s = Sor()
    s.append(1)
    s.append(3)
    s.append(5)
    print(s.size())
    print(s.ures())
    print(s.popleft())
    s.append(9)
    print(s.popleft())


if __name__ == "__main__":
    main()
