"""solution"""

if __name__ == "__main__":
    INPUT_STRING = input()
    LENGTH = len(INPUT_STRING)
    RESULT = ""

    """selecting substring with the length: len(string) = x * len(substring),
    where x is Natural number and checking the equality"""

    for x in range(LENGTH):
        sample = INPUT_STRING[:(LENGTH - x)]
        sample_length = len(sample)
        if LENGTH % sample_length != 0:
            continue
        num = LENGTH / sample_length
        if sample * int(num) == INPUT_STRING:
            RESULT = num
        else:
            continue

    print(int(RESULT))
