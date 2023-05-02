#!/usr/bin/env python3

from enum import Enum


class Hangrend(Enum):
    MELY = ["a", "á", "o", "ó", "u", "ú"]
    MAGAS = ["e", "é", "i", "í", "ö", "ő", "ü", "ű"]


def hangrend(word):
    ans = ""
    magas = 0
    mely = 0
    for i in word:
        if i in Hangrend.MELY.value:
            mely = 1
        elif i in Hangrend.MAGAS.value:
            magas = 1
        else:
            ans = "semmilyen"
    if mely == 1 and magas == 1:
        ans = "vegyes"
    elif mely == 1 and magas == 0:
        ans = "mély"
    elif mely == 0 and magas == 1:
        ans = "magas"
    return f"A {word} szó {ans} hangrendű!"


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "gfflkptz"]
    for i in words:
        print(hangrend(i))


if __name__ == "__main__":
    main()
