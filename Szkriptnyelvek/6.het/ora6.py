#!usr/bin/env python3

import sys

def main():


    d = {} #üres szótár
    d["a"] = "alfa"
    d["b"] = "beta"
    d["g"] = "gamma"
    print(d)


    print(d["b"])
    d.get("a")
    #ha olyan értékre getelek ami nics benne a szótárba None-t ad vissza
    d.get("a","nincs benne") #a benne van a szótárba alfa-t adja vissza
    d.get("x","nincs benne") # x nincs benne a szótárba a nincs bennével fog visszatérni


    
    #Minden kulcshoz lista tartozik
    k='a'
    for e in d.get(k,[]):
        pass
    

    if "a" in d:
        print("a benne van")
    
    d["a"]="ALFA"
    print(d["a"])


    d.keys() #iterátor egyenként adja vissza az elemeket pl for ciklusban
    list(d.keys()) #liszt() iterátorokat gyűjt össze listává
    list(d.values())
    print("reeeeeeeeeeeeeeeeee")

    for e in d:
        print(e + "->" + d[e])
        print(list(d.items()))
    print()

    for k,v in d.items():
        print(k,"->",v)

    print()
    d["o"]="omega"
    d["d"]="delta"

    #rendezett listába vissza kapni a kulcsokat
    print(sorted(d.keys()))


    #elemet törölni szótárból, a kulcsot és a hozzátartozó értéket is törli
    del d["b"]
    print()



    f=open("valami.txt","r")    #az r a read ha írni akarnék akkor "w" lenne az "r" helyén
    for line in f:
        #line=line.rstrip("\n") így is lehetne az end helyett
        print(line,end="")  #ha az end-et namrakjuk oda dupla sortörés lesz mert a fájlban is van meg a print is ra k oda egyet
    
        for line in f:
            line.endswith("sor.")#semmi nem lesz a kimenet mert a végén ott a sortörés
            #ha wbe nyitok meg valamit addigi tartalom elvész a fájlba
    f.close()





    f=open("valami.txt","r")
    
    sorok=f.readlines()
    print(sorok)

    f.close()





    f=open("valami.txt","r")

    content=f.read()    #ebbe még benne vannak
    sorok=content.splitlines() #sortörések ebbe nem lesznek
    print(sorok)
    #print("'" + content + "'") #egyetlen strngként vissza adja a ffájl tartalmát





    #Fájlba írás
    f=open("out.txt","w")
    print("hello",file=f)
    print("world",file=f)
    f.write("aa\n") #nem rak bele sortörést csak ha te oda teszed mint most
    f.close() #eddig pufferbe írunk 8kb pl a buffer ha megtelik kiírja szóval ha ezt lehagyjuk akkor lehet a vége hiányozni fog
    sys.stdout.write("hsd")


if __name__=='__main__':
    main()