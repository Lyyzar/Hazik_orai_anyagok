#!usr/bin/env python3


def find_words(li):
    
    result = []
    for word in li:
        if 'j' in word and 's' in word and 'u' in word and 'n' in word:

            index_j = word.index('j')
            index_s = word.find('s', index_j)
            index_u = word.find('u', index_s)
            index_n = word.find('n', index_u)
            if index_j < index_s < index_u < index_n:
                result.append(word)
    return result


def main():

    f = open("DT2.csv","r",encoding='utf-8')
    li=f.readlines()
    jo_list = list()
    for row in li:
        jo_list.append(row[0:row.find(',')])
    

    print(find_words(jo_list))

    

if __name__ == '__main__':
    main()