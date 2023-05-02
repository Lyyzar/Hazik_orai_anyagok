#!usr/bin/env python3


def munsch(num):
    for i in range(num):
        res=0
        for chars in str(i):
            num=int(chars)
            if num==0:
                res+=1
            else:
                res+=num**num
        if res==i:
            print("Megoldás:",i)


def main():
    munsch(440000000)


if __name__=='__main__':
    main()