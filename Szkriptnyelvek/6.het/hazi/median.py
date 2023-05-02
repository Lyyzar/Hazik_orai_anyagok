#!usr/bin/env python3

def median(numbers:list[int]) -> int:
    res:int=0
    li:list[int]=[]
    if len(numbers)%2==0:
        li=sorted(numbers)
        res=(li[len(li)//2-1]+li[(len(li)//2)])/2    
    else:
        li=sorted(numbers)
        res=li[(len(li)-1)//2]
    return res
        


def main():
    print(median([1, 2, 3, 4, 5]))
    print(median([3, 1, 2, 5, 3]))
    print(median([1, 300, 2, 200, 1]))
    print(median([3, 6, 20, 99, 10, 15]))
    



if __name__=='__main__':
    main()