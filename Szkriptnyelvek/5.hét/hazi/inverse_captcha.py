#! usr/bin/env python3

def inv_cap(s):
    """This function adds together numbers that are followed by the same number"""
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
    print(inv_cap(1111))


if __name__=='__main__':
    main()