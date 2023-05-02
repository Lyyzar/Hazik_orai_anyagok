#!usr/bin/env python3

def ekezet_clear(lines):
    d={
        "á" : "a","é" : "e","í" : "i","ó" : "o","ő" : "o","ü" : "u","ű" : "u","ú" : "u","ö" : "o",
        "Á" : "A","É" : "E","Í" : "I","Ó" : "O","Ő" : "O","Ü" : "U","Ű" : "U","Ú" : "U","Ö" : "O",
    }
    res=""
    for character in lines:
        if character in d:
         res+=d[character]
        else:
           res+=character
    return res 



TEXT="""
A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
"""

def main():
    
    print(ekezet_clear(TEXT))
    
    
    




if __name__=='__main__':
    main()