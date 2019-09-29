#create a dictionary.
d = {}
#reading and inserting keys(words) with appropriate value(number of use).
while 1:
    line = input().split()
    if (not line) :
        break
    for string in line:
        if (string) :
            if (string in d) :
                d[string] += int(1)
            else :
                d[string] = int(1)
        else :
            break
flag = 0
max = 0
#searching for the most common word.
for word in d:
    if (d[word] == max) :
        flag = 1
    if (d[word] > max) :
        max = d[word]
        result = word
        flag = 0

if (flag == 1) :
    print('-')
else :
    print(result)