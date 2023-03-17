#! usr/bin/env python3

def ciklus(number,debug=False):
    f=[i for i in range(1,number)]
    if debug:
        print("#Ciklus kezdete")
    print(f)
    
    if debug:
        print("#Ciklus vége")


def main():
    ciklus(10)
    ciklus(10,True)


if __name__=='__main__':
    main()