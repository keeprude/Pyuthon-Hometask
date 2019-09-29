from itertools import product

def combinations (num) :
    dictionary = {0 : ('_'), 1 : (''), 2 : ('a', 'b', 'c'), 3 : ('d', 'e', 'f'), 4 : ('g', 'h', 'i'),
        5 : ('j', 'k', 'l'), 6 : ('m', 'n', 'o'), 7 : ('p', 'q', 'r', 's'), 
        8 : ('t', 'u', 'v'), 9 : ('w', 'x', 'y', 'z')}
    arrays = []
    for x in num :
        if (x == '1') :
            continue
        arrays.append(dictionary[int(x)])
    temp = list(product(*arrays))
    result = []
    for pair in temp :
        result.append(''.join(pair))
    print(result)

x = input()
combinations(x)