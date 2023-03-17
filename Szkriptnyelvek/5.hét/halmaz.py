#! usr/bin/env python3

def main():
    #HALMAZOK
    kosar=["alma","narancs","banan","alma","narancs","banan"]
    gyumolcs= set(kosar)
    print(kosar)
    print(gyumolcs)

    numbers=[5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]
    a=sorted(set(numbers))
    print(a)


    k=["alma","banán","citrom"]
    print(k)
    b=set()
    print(b)
    b.add("banán")
    b.add("narancs")
    print(b)

    k=set(k)
    k.intersection(b) #új halmazt ad vissza
    k.union(b)
    k.difference(b)
    k.remove("alma")



if __name__=='__main__':
    main()