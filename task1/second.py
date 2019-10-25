"""solution"""

import first

def sum_of_two_lists(list1, list2):
    """impementation of sum of two lists"""

    term1 = list1.first
    term2 = list2.first
    if term1 is None:
        return term2
    if term2 is None:
        return term1
    temp_result_list = first.SinglyLinkedList()
    flag = 0

    while term1 is not None and term2 is not None:
        temp_result_list.add((term1.value + term2.value + flag) % 10)
        if term1.value + term2.value + flag >= 10:
            flag = 1
        else:
            flag = 0
        term1 = term1.next
        term2 = term2.next

    if term1 is None and term2 is None:
        return temp_result_list

    if term1 is None and term2 is not None:
        while term2 is not None:
            temp_result_list.add((term2.value + flag) % 10)
            if term2.value + flag >= 10:
                flag = 1
            else:
                flag = 0
            term2 = term2.next
    elif term1 is not None and term2 is None:
        while term1 is not None:
            temp_result_list.add((term1.value + flag) % 10)
            if term1.value + flag >= 10:
                flag = 1
            else:
                flag = 0
            term1 = term1.next

    if flag == 1:
        temp_result_list.add(int(1))
    return temp_result_list

FIRST_NUMBER = input()
SECOND_NUMBER = input()
MY_LIST_1 = first.into_list(FIRST_NUMBER)
MY_LIST_2 = first.into_list(SECOND_NUMBER)
RESULT_LIST = []
RESULT_LIST = sum_of_two_lists(MY_LIST_1, MY_LIST_2)
RESULT_LIST.print()
