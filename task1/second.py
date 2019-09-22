import first

def sum (list1, list2):
    term1 = list1.first
    term2 = list2.first
    if term1 == None :
        return term2
    if term2 == None :
        return term1
    resultlist = first.SinglyLinkedList()
    flag = 0
    while (term1 != None) and (term2 != None) :
        resultlist.add((term1.value + term2.value + flag) % 10)
        if (term1.value + term2.value + flag >= 10) :
            flag = 1
        else :
            flag = 0
        term1 = term1.next
        term2 = term2.next
    if (term1 == None and term2 == None) :
        return resultlist
    if (term1 == None and term2 != None) :
        while (term2 != None) :
            resultlist.add((term2.value + flag) % 10)
            if (term2.value + flag >= 10) :
                flag = 1
            else:
                flag = 0
            term2 = term2.next
    elif (term1 != None and term2 == None) :
        while (term1 != None) :
            resultlist.add((term1.value + flag) % 10)
            if (term1.value + flag >= 10) :
                flag = 1
            else:
                flag = 0
            term1 = term1.next
    if (flag == 1) :
        resultlist.add(int(1))
    return resultlist

x = input()
y = input()
list1 = first.IntoList(x)
list2 = first.IntoList(y)
list = sum(list1, list2)
list.print()