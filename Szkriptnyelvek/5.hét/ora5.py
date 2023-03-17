#! usr/bin/env python3

import sys

def greet(name,greetings="Hello"):  #name kötelező érték, aminek adunk alap értéket az opcionális mint itt a greetings
    print(f"{greetings} {name}!")

def main():
    greet("gr")
    greet("prrt",greetings="Hola")
    greet("prrt",greetings="Bonjour")

    stt="hello world ldld"
    g=[len(s) for s in stt.split(" ")]
    print(g)

    l=[i for i in range(2,21,2)]
    print(l)
    k=[i*2 for i in range(1,11)]
    print(k)
    c=list(range(2,21,2))
    print(c)

    #metódus class metódusok, példány metódusok
    #függvény amit mi írunk pl


    #Óra anyaga:

    #Python 2be jobban látszik
    a=sys.maxsize
    print(type(a))
    print(a)
    b=a+1
    print(b)
    print(type(b))


    #Python3:
    #Integer a long típus is nincs rá külön type


    li=["alfa", "beta", "gamma"]


    #Ki akarjuk íni az elemeket az indexeikkel együtt
    for indx,e in list(enumerate(li, start=1 )):     #Erre használjuk az enumerate függvényt tuple-öket ad vissza
        print(indx,e)               #A start 1 től kezdi az indexelést


    #Van break
    #Van continue is ami ha pl if i ==2 után van egy continue nem fut le
    #az alatta lévő dolog hanem megy a kövi i értékre


    #Ha nem írtad még meg a függvényt stb megadhatod a [pass] szót és nem veszi hibának

    #docstring --> függvény elején rövid leírás mit csinál def után első sorba """Return the square root of 2."""
    #Függvény docstringjét le is lehet kérdezni függvény_név.__doc__    Parancssorból a help is kiiratja











if __name__=='__main__':
    main()