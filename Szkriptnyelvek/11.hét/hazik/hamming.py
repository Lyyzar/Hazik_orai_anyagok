#!usr/bin/env python3

def hamming(word1:str,word2:str) -> int:
    res:int=0
    for i in range(len(word1)):
        if word1[i]==word2[i]:
            continue
        else:
            res+=1
    response(word1,word2,res)
    return res

def response(w1:str,w2:str,num:int) -> None:
    print(f"A {w1} és {w2} szó hamming távolsága: {num}")

def main():
    hamming("lecke","pecke")
    hamming("keceja","valami")
    hamming("holv","hlov")
    hamming("","")
    hamming("kétszer","egyszer")
    

if __name__ == '__main__':
    main()