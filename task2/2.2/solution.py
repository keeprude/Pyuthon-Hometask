"""solution"""

if __name__ == "__main__":
    DICT = {}
    #reading and inserting keys(words) with appropriate value(number of use).
    while 1:
        LINE = input().split()
        if not LINE:
            break
        for string in LINE:
            if string:
                if string in DICT:
                    DICT[string] += int(1)
                else:
                    DICT[string] = int(1)
            else:
                break
    FLAG = 0
    MAX_NUMBER_OF_USE = 0
    RESULT = ""
    #searching for the most common word.
    for word in DICT:
        if DICT[word] == MAX_NUMBER_OF_USE:
            FLAG = 1
        if DICT[word] > MAX_NUMBER_OF_USE:
            MAX_NUMBER_OF_USE = DICT[word]
            RESULT = word
            FLAG = 0

    if FLAG == 1:
        print('-')
    else:
        print(RESULT)
