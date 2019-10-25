"""solution"""

from itertools import product

def combinations(num):
    """prints all the possible combinations of letters"""

    dictionary = {0 : ('_'),
                  1 : (''),
                  2 : ('a', 'b', 'c'),
                  3 : ('d', 'e', 'f'),
                  4 : ('g', 'h', 'i'),
                  5 : ('j', 'k', 'l'),
                  6 : ('m', 'n', 'o'),
                  7 : ('p', 'q', 'r', 's'),
                  8 : ('t', 'u', 'v'),
                  9 : ('w', 'x', 'y', 'z')}
    arrays = []
    for digit in num:
        if digit == '1':
            continue
        arrays.append(dictionary[int(digit)])
    temp = list(product(*arrays))
    result = []
    for pair in temp:
        result.append(''.join(pair))
    print(result)

if __name__ == "__main__":
    INPUT_NUMBER = input()
    combinations(INPUT_NUMBER)
