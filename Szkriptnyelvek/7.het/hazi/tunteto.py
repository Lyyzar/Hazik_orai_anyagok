#!usr/bin/env python3
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd ='C:\Program Files\Tesseract-OCR\\tesseract.exe'

def ocr_text(img):
    text=pytesseract.image_to_string(img)
    return text


def main():
    img=cv2.imread('tunteto.jpg')
    s=ocr_text(img).split()
    #rosszul olvassa be vannak benne 9-esek meg @ és más karakterek
    print(s)
    text=[b"01111001",b"01101111",b"01110101",b"01110100",b"01110101",b"00101110",b"01100010",b"01100101",b"00101111",b"01100100",b"01010001",b"01110111",b"00110100",b"01110111",b"00111001",b"01010111",b"01100111",b"01011000",b"01100011",b"01010001"]
    result=""
    for word in text:
        n = int(word, 2)
        result+=n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    print(result)


if __name__=='__main__':
    main()