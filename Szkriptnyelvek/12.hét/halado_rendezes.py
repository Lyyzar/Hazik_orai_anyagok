#!usr/bin/env python3

def sorter(tup):
    return tup[-1]

def sort_forusers(li):
    
    return int(li.split(':')[0])

def sorter_forlist(li):
    return li[1]

def main():
    data=[
        (1, 'Albany','NY',162692),
        (3, 'Allegany','NY',11986),
        (121, 'Wyoming','NY',8722),
        (123, 'Albany','NY',5094)
    ]
    print(sorted(data,key=sorter))


    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print(users)
    print(sorted(users,key=sort_forusers))



    li = [[2,6], [1,3], [5,4]]
    print(li)
    print(sorted(li,key=sorter_forlist))


if __name__ == '__main__':
    main()