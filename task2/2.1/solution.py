s = input()
length = len(s)
#selecting substring with the length: len(string) = x * len(substring), where x is Natural number and 
#checking the equality.
for x in range(length) :
    sample = s[:(length - x)]
    sample_length = len(sample)
    if (length % sample_length != 0) :
        continue
    num = length / sample_length
    if (sample * int(num) == s) :
        result = num
    else :
        continue

print(int(result))
    