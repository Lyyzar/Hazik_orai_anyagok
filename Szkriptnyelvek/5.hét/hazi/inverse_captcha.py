#! usr/bin/env python3

def m(s):
    k=str(s)
    res=0
    for inx,num in enumerate(k):
        if inx+1>=len(k):
            inx=0
            if num==k[inx]:
                res+=int(num)
        else:
            if num==k[inx+1]:
                res+=int(num)
    return res

def main():
    print(m(1111))


if __name__=='__main__':
    main()