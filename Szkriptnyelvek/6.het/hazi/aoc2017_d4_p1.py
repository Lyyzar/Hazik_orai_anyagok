#!usr/bin/env python3

def valami(filenev):
    f=open(filenev,"r")
    benne=set()
    for line in f:
        words=line.split()
        for index,phrase in enumerate(words):
            if phrase in benne:
                print(f"Nem jó phrase a  --{line}")
            else:
                benne.add(phrase)
                if index==len(words)-1 and phrase not in benne:
                    print(f"Jó phrase a --{line}")
    f.close()
    


def main():
    print(valami("day04.txt"))

   
if __name__=='__main__':
    main()