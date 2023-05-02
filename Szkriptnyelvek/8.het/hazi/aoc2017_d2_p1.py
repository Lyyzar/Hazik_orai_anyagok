#!usr/bin/env python3


def checksum(file):
    li = list()
    f = open(file)
    for num in f:
        li.append(num.split())
    f.close()
    res = 0
    for l in li:
        l = [int(x) for x in l]
        res += max(l) - min(l)
    return res


def main():
    print(checksum("day02.txt"))


if __name__ == "__main__":
    main()
