#!usr/bin/env python3

import pygyak as pgy
#from pygyak import is_prime    lehet úgy használni hogy csaka függvény nevet használom nem kell a modult is hozzá pontozi

import random


def randch(li):
    index=random.randint(0,len(li)-1)
    return li[index]




def shuffled(li): #nem helyben rendez hanem egy másolatot ad vissza
    #lu=li #a lu referencia a li által referált listára tehát ugyanúgy módosul
    #helyes megoldáás:
    lu=li[:]            #vagy lu=li.copy()
    random.shuffle(lu)
    return lu

def main():
    #típus annotációk (s:str) -> Array ezt adja vissza

    primek=[]
    for i in range(1,100):
        if pgy.is_prime(i):
            primek.append(i)
    print(primek)
    #100nal kisebb primek

    primek_ossz=0
    for i in range(1,200):
        if pgy.is_prime(i):
            primek_ossz+=i
    print(primek_ossz)
    #ketszaznal kisebb primek osszege

    print(random.random())
    print(random.randint(1,5)) #itt zárt az intervallum 1 és 5 között
    print(random.randrange(1,5)) #itt már ugyanolyan mint a range, tehát jobbról nyílt

    li=[5,6,7,4,2,1]
    print(random.shuffle(li)) #nem függvény hanem eljárás nem ad vissza semmit (None)
    print(li)

    print(shuffled(li)[-1])

    random.choice(li) #egy listából egy random elemet ad vissza

    lk=[123,543,765,34,56,234]
    print(randch(lk))


if __name__=='__main__':
    main()