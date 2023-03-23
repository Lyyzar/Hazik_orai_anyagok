#!usr/bin/env python3
import sys



def main():
    f=open("valami.txt","r")
    k=open("out.txt",'w')

    for line in f:
        k.write(line)


    #gdgr.copy(mit,hova)

    f.close()
    k.close()



if __name__=='__main__':
    main()