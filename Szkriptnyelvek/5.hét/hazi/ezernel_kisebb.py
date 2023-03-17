#! /usr/bin/env python3

def szamok_osszege():
    """Gives back a sum of a list where the elements of the list are less then 1000 and divisible by 3 or 5"""
    li=[]
    for i in range(1,1000):
        if i%3==0 or i%5==0:
            li.append(i)
    return sum(li)
def main():
    print(szamok_osszege())
    li=[i for i in range(1,1000) if i%3==0 or i%5==0]
    print(sum(li))

if __name__=='__main__':
    main()