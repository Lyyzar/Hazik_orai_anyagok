#!usr/bin/env python3

def anagramma(first:str,second:str) -> bool:
    res:bool=True
    hp:set[str]=set()
    
    for ch in first:
        hp.add(ch)
    for character in second:
        if character not in hp:
            res=False
    return res


def main():
    print(anagramma("listen","silent"))
    print(anagramma("egymás","sámga"))
    print(anagramma("dormitory","dirty room"))
 
if __name__=='__main__':
    main()