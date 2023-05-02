#!usr/bin/env python3

default="""| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
| . . . . . . . . |
"""

def kiralyno(li):
    d={0:2,1:4,2:6,3:8,4:10,5:12,6:14,7:16}
    table=default.split("\n")
    for index,q in enumerate(li):
            table[abs(q-7)]=table[abs(q-7)][:d[index]] + 'Q' + table[abs(q-7)][d[index]+1:]
    print("+-----------------+")
    for i in table:
        print(i)
    print("+-----------------+")
            




def main():
    kiralyno([7,3,0,2,5,1,6,4])
    kiralyno([0,4,7,5,2,6,1,3])

if __name__=='__main__':
    main()