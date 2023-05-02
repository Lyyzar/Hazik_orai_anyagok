#!usr/bin/env python3

def main():
    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = list(range(ord('a'),ord('z')+1))

    for t in range(len(chars)):
        print((chars[t],codes[t]))


if __name__=='__main__':
    main()