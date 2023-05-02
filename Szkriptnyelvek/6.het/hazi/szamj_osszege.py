#!usr/bin/env python3

def szamj_ossz(number):
    mynum=2**number
    res=0
    for ch in str(mynum):
        res+=int(ch)
    return res


def main():
    print(szamj_ossz(15))
    print(szamj_ossz(1000))
 
 
if __name__=='__main__':
    main()