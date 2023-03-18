#! usr/bin/env python3

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """A 2 parameter function, it gives back a string. It's looking for characters from the second parameter in the first parameter, if it finds one concatenate it"""
    res=""
    for s in text:
        for p in chars:
            if s==p:
                res+=s
    return res

def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))
    print(valid("ABVDADS"))



if __name__=='__main__':
    main()